import streamlit as st
from streamlit_url_fragments import get_fragments
from supabase import create_client

from settings import settings


def use_custom_css():
    with open("custom.css") as custom_css:
        return st.write(f'<style>{custom_css.read()}</style>', unsafe_allow_html=True)


def check_openai_key():
    if st.session_state.get("api_success", False) is False:
        st.warning("""
        No OpenAI key was found! If you don't set the OpenAI Key, none of the exercises here will work.
        """, icon="🤦‍♀️")
        with st.form("openai_key_form"):
            st.subheader("Enter your OpenAI API Key")
            st.text_input("OpenAI API Key", placeholder="sk-...", key="openai_key")

            submitted = st.form_submit_button("Submit")

            if submitted:
                from openai import AuthenticationError
                try:
                    import openai
                    openai.api_key = st.session_state.openai_key
                    openai.Model.list()
                except AuthenticationError:
                    st.session_state["api_success"] = False
                    st.error(
                        "An incorrect API Key was provided. You can find your API key at "
                        "https://platform.openai.com/account/api-keys."
                    )
                    return
                st.session_state["api_success"] = True
                st.success("Success! You are good to go.", icon="🎉")


def write_footer():
    st.divider()
    st.write(
        """
Prompt Engineering for Lawyers © 2023 by Ang Hou Fu is licensed under Attribution-ShareAlike 4.0 International  
[![Repo](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/houfu/prompt-engineering-lawyers) 
        """
    )


supabase_client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)


def is_supabase_session_params(obj: dict):
    required_keys = {
        "access_token": str,
        "refresh_token": str,
    }

    # Check for the presence of all required keys and their types
    for key, expected_type in required_keys.items():
        if not (not (key not in obj) and isinstance(obj[key], expected_type)):
            return False

    return True


def welcome_mat():
    """
    Checks whether the user is logged in and sets the session state accordingly
    :return:
    """
    if "logged_in" not in st.session_state or st.session_state["logged_in"] is False:
        session_params = get_fragments()

        if session_params:
            if is_supabase_session_params(session_params):
                try:
                    supabase_client.auth.set_session(session_params["access_token"], session_params["refresh_token"])
                    supabase_client.auth.get_user()
                except Exception as e:
                    st.error(f"An error occurred: {e}")
                st.session_state["logged_in"] = True
        else:
            st.session_state["logged_in"] = False


def log_out():
    supabase_client.auth.sign_out()
    st.session_state["logged_in"] = False
    st.session_state["api_success"] = False
    st.query_params.clear()
