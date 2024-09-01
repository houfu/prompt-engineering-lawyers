from typing import Optional

import streamlit as st
from streamlit_url_fragments import get_fragments
from supabase import create_client

from settings import settings


def use_custom_css():
    with open("custom.css") as custom_css:
        return st.write(f'<style>{custom_css.read()}</style>', unsafe_allow_html=True)


def check_openai_key():
    if st.session_state.get("openai_key", None) is None:
        st.warning("""
        No OpenAI key was found! If you don't set the OpenAI Key, none of the exercises here will work.
        """, icon="🤦‍♀️")
        with st.form("openai_key_form"):
            st.subheader("Enter your OpenAI API Key")
            st.text_input("OpenAI API Key", placeholder="sk-...", key="openai_key_input")

            submitted = st.form_submit_button("Submit")

            if submitted:
                from openai import AuthenticationError
                try:
                    import openai
                    client = openai.Client(api_key=st.session_state.openai_key_input)
                    client.models.list()
                except AuthenticationError:
                    st.error(
                        "An incorrect API Key was provided. You can find your API key at "
                        "https://platform.openai.com/account/api-keys."
                    )
                    return
                st.session_state["openai_key"] = st.session_state.openai_key_input
                st.success("Success! You are good to go.", icon="🎉")


def write_footer():
    st.divider()
    st.write(
        """
Prompt Engineering for Lawyers © 2023-2024 by Ang Hou Fu is licensed under Attribution-ShareAlike 4.0 International  
[![Repo](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/houfu/prompt-engineering-lawyers) 
        """
    )
    st.html('<a href="https://www.buymeacoffee.com/houfu"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a kopi (siu dai)&emoji=☕&slug=houfu&button_colour=5F7FFF&font_colour=ffffff&font_family=Lato&outline_colour=000000&coffee_colour=FFDD00" /></a>')


def write_essay_page():
    st.info("This page does not contain any prompt engineering exercises. If you are looking for _exercises_ "
            "and _applications_, you may want to move to the next page.", icon="📝")


def write_what_you_will_learn(learnings: list[str]):
    learnings_md_list = "\n".join(f"* {learning}" for learning in learnings)
    st.success(f"""
✍️ What you will learn in this section:
---------------------------------------
    
{learnings_md_list}
""")


def write_more_resources(resources: list[str]):
    resources_md_list = "\n".join(f"* {resource}" for resource in resources)
    st.info(f"""
 📚 Further reading and resources:
---------------------------------------
    
{resources_md_list}
""")


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
    st.session_state["openai_key"] = None
    st.query_params.clear()


def navigation_footer(page_path: str):

    st.divider()

    from routes import get_routes_list
    routes = get_routes_list()

    def search_route_index_by_path(path: str) -> (int, Optional[st.Page]):
        for index, page in enumerate(routes):
            if page.path == path:
                return index, page
        return -1, None

    page_index, page_page = search_route_index_by_path(page_path)
    if page_index > 0:
        if page_index == len(routes) - 1:
            col1, col2 = st.columns(2)
            with col1:
                previous_page = routes[page_index - 1]
                st.page_link(f"{previous_page.path}", label=f"_{previous_page.title}_", icon="⬅️")
            with col2:
                st.page_link("content/pages/Home.py", label="Home", icon="🏠")
        else:
            col1, col2, col3 = st.columns(3)
            with col1:
                previous_page = routes[page_index - 1]
                st.page_link(f"{previous_page.path}", label=f"_{previous_page.title}_", icon="⬅️")
            with col2:
                st.page_link("content/pages/Home.py", label="Home", icon="🏠")
            with col3:
                next_page = routes[page_index + 1]
                st.page_link(f"{next_page.path}", label=f"_{next_page.title}_", icon="➡️")
    elif page_index == 0:
        col1, col2 = st.columns(2)
        with col1:
            st.page_link("content/pages/Home.py", label="Home", icon="🏠")
        with col2:
            next_page = routes[page_index + 1]
            st.page_link(f"{next_page.path}", label=f"_{next_page.title}_", icon="➡️")