from datetime import datetime
from typing import TypedDict, Union

import streamlit as st

from helpers import supabase_client


class User(TypedDict):
    id: str
    email: str
    last_sign_in_at: Union[datetime, None]


def is_authenticated_user() -> Union[User, None]:
    user = supabase_client().auth.get_user()
    if not user:
        return None
    else:
        user_dict = user.dict()
        return {
            "id": user_dict["id"],
            "email": user_dict["email"],
            "last_sign_in_at": user_dict["last_sign_in_at"],
        }


def welcome_mat():
    if user := is_authenticated_user():
        st.write("---")
        st.write(f"### Welcome back, {user['email']}!")
        st.write(f"Last signed in at: {user['last_sign_in_at']}")
        st.write("---")
    else:
        with st.form(key="sign_in_form"):
            st.write(":material/login:**Sign in to experience the full features of this site.**")
            email = st.text_input("Email")
            submitted = st.form_submit_button("Sign In")

            if submitted:
                # Check whether user is already has access; if yes, proceed to send magiclink.
                # If not, encourage user to buy.
                from gotrue.errors import AuthApiError

                try:
                    supabase_client().auth.sign_in_with_otp(
                        {
                            "email": email,
                            "options": {
                                "should_create_user": False,
                                # "captcha_token":
                            },
                        }
                    )
                    st.success(
                        "A link to login to the website has been sent to your email. "
                        "Please check your spam if you don't see it."
                    )
                except AuthApiError:
                    st.error(
                        "You need to sign in using the email address you used to purchase access."
                    )

            st.caption("""
            To be able to sign in, you need to purchase access to the course through this link.
            Some of the content is available for free, so you can check that out before making a purchase.
            """)


def is_supabase_session_params(obj: dict) -> bool:
    required_keys = {
        "access_token": str,
        "refresh_token": str,
    }

    # Check for the presence of all required keys and their types
    for key, expected_type in required_keys.items():
        if not (not (key not in obj) and isinstance(obj[key], expected_type)):
            return False

    return True
