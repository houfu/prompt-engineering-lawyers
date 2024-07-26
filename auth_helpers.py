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
            "last_sign_in_at": user_dict["last_sign_in_at"]
        }


def welcome_mat():
    st.write("---")
    if user := is_authenticated_user():
        st.write(f"### Welcome back, {user['email']}!")
        st.write(f"Last signed in at: {user['last_sign_in_at']}")
    else:
        st.write("### To experience the full content of this site, you should sign in.")
        with st.form(key="sign_in_form"):
            email = st.text_input("Email")
            submitted = st.form_submit_button("Sign In")

            if submitted:
                # Check whether user is already has access; if yes, proceed to send magiclink.
                # If not, encourage user to buy.
                supabase_client().table()
    st.write("---")

