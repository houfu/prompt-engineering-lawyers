import streamlit as st

from helpers import use_custom_css, write_footer, welcome_mat, log_out

st.set_page_config(layout="wide")

if "api_success" not in st.session_state:
    st.session_state["api_success"] = False

welcome_mat()

use_custom_css()


pg = st.navigation(
    {
        "": [
            st.Page("content/pages/Home.py", title="Home", default=True),
        ],
        "Getting Started": [
            st.Page("content/pages/introduction.py", title="Introduction"),
        ],
    }
)
pg.run()


with st.sidebar:
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

write_footer()
