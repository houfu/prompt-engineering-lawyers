import streamlit as st

from helpers import supabase_client
from routes import get_navigation

st.image("content/reading_bar.png", use_column_width=True)

st.title("Prompt Engineering for Lawyers")

"""
*Explore the possibilities of prompt engineering and large language models in the legal domain.*
"""

if st.session_state["logged_in"]:
    st.success("You are logged in! :tada: Continue your journey.")
else:
    st.info("You are not logged in. Please log in to access the full course.")

    with st.form(key="sign_in_form"):
        st.write(":material/login:**Sign in to experience the full features of this site.**")
        email = st.text_input("Email", help="This only works if you have already subscribed to this site.")
        submitted = st.form_submit_button("Sign In")

        if submitted:
            # Check whether user is already has access; if yes, proceed to send magiclink.
            # If not, encourage user to buy.
            from gotrue.errors import AuthApiError

            try:
                supabase_client.auth.sign_in_with_otp(
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
                    "You can't sign in unless you have already subscribed to this site."
                )

    get_navigation()

    st.header("Having Trouble?")
    """
    You can still continue to browse the site without logging in, but not all its feature will be available to you.
    """
    st.page_link("content/pages/about_this_site.py", label="Why should I subscribe?", icon="💁‍♂️")

    st.page_link("https://buymeacoffee.com/houfu/membership", label="**Subscribe to this site**", icon="👉")
