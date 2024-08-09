import streamlit as st
from streamlit_url_fragments import get_fragments

from auth_helpers import is_supabase_session_params, is_authenticated_user
from helpers import use_custom_css, write_footer, supabase_client
from routes_helper import get_pages
from db import engine, SQLModel

SQLModel.metadata.create_all(engine)

if "supabase_session" not in st.session_state:
    session_params = get_fragments()
    if session_params and is_supabase_session_params(session_params):
        st.session_state["supabase_session"] = session_params
        # Run the function to initialize the connection.
        supabase_client()


if "api_success" not in st.session_state:
    st.session_state["api_success"] = False

use_custom_css()

pg = st.navigation(get_pages(is_authenticated_user() is True))
pg.run()

write_footer()
