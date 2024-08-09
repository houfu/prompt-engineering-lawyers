import streamlit as st

from helpers import use_custom_css, write_footer

st.set_page_config(layout="wide")

if "api_success" not in st.session_state:
    st.session_state["api_success"] = False

use_custom_css()

pg = st.navigation({
    "": [
        st.Page("pages/Home.py", title="Home", default=True),
    ],
    "Getting Started": [
        st.Page("pages/introduction.py", title="Introduction"),
    ]
}
)
pg.run()


write_footer()
