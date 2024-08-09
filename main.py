import streamlit as st

from helpers import use_custom_css, write_footer

if "api_success" not in st.session_state:
    st.session_state["api_success"] = False

use_custom_css()

pg = st.navigation([
    st.Page("pages/Home.py")
])
pg.run()


write_footer()
