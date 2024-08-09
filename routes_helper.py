import streamlit as st
from sqlmodel import select, Session
from streamlit.navigation.page import StreamlitPage

from db import engine
from models import Section


def get_page_icon(logged_in, locked) -> str:
    if logged_in:
        return "🔒" if locked else "🔓"
    else:
        return "🔒" if locked else "🔓"


def get_pages(logged_in: bool) -> dict[str, list[StreamlitPage]]:
    result = {}

    with Session(engine) as db:
        statement = select(Section)
        sections = db.exec(statement)

        for idx, section in enumerate(sections):
            section_pages = [page for page in section.pages if page.active]
            section_pages.sort(key=lambda x: x.page_order)
            result[section.title] = [
                st.Page(
                    f"pages/{page.path}",
                    title=page.title,
                    icon=get_page_icon(logged_in, page.locked),
                )
                for page in section_pages
            ]

    return result
