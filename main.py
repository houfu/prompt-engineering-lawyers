import streamlit as st

from helpers import use_custom_css, write_footer, welcome_mat, log_out
from routes import get_routes, get_navigation

st.set_page_config(layout="wide")

if "openai_key" not in st.session_state:
    st.session_state["openai_key"] = None

welcome_mat()

use_custom_css()


pg = st.navigation(get_routes(), position="hidden")
pg.run()


with st.sidebar:
    st.title("Prompt Engineering for Lawyers by Ang Hou Fu")
    if st.session_state["logged_in"]:
        st.write("You are logged in! :tada:")
        st.button("Log out", on_click=lambda: log_out())
    else:
        st.write("You are not logged in.")
        st.page_link(
            "content/pages/Home.py",
            label="Please log in.",
            icon=":material/login:",
        )
        st.page_link(
            "https://buymeacoffee.com/houfu/membership",
            label="**Subscribe to this site**",
            icon="👉",
        )
    get_navigation()

write_footer()
