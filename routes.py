from typing import Optional

import streamlit as st
from pydantic import BaseModel, Field


class Section(BaseModel):
    id: Optional[int] = Field(default=None)
    title: str = Field(default="New Section", description="Title of the Section")
    section_order: int = 0
    pages: list["Page"]


class Page(BaseModel):
    id: Optional[int] = Field(default=None)
    title: str = Field(default="New Page", description="Title of the page")
    locked: bool = Field(
        default=False, description="Whether being a user is needed to view the page"
    )
    page_order: int = 0
    active: bool = Field(default=True, description="Whether the page is active")
    beta: bool = Field(default=False, description="Whether the page is in beta")
    path: str = Field(default="pages/test.py", description="Path to the page")


data_pages = [
    Section(
        section_order=0,
        pages=[
            # Home
            Page(
                title="Home",
                page_order=0,
                path="content/pages/Home.py",
            )
        ]
    ),
    Section(
        title="Preliminaries",
        section_order=1,
        pages=[
            # Introduction
            Page(
                title="About this Site",
                page_order=0,
                path="content/pages/about_this_site.py",
            ),
            # What is Prompt Engineering?
            Page(
                title="What is Prompt Engineering?",
                page_order=1,
                path="content/pages/what_is_prompt_engineering.py",
                beta=True,
            )
        ],
    ),
    Section(
        title="Getting Started",
        section_order=2,
        pages=[
            # Completion
            Page(
                title="From Prompt to Completion",
                page_order=0,
                path="content/pages/completion.py",
            ),
            # Everything in its Context
            Page(
                title="Everything in its Right Context",
                page_order=1,
                path="content/pages/everything_in_context.py",
            ),
            # Now this! Using LLMs for rewriting
            Page(
                title="Now this! Transforming text using LLMs.",
                page_order=2,
                path="content/pages/now_this.py",
            ),
            # Chat as memory
            Page(
                title="Chat as Memory",
                page_order=3,
                path="content/pages/chat_as_memory.py",
            ),
            # A role for the System
            Page(
                title="A role for the System",
                page_order=4,
                path="content/pages/a_role_for_the_system.py",
            ),
        ],
    ),
    Section(
        title="Transforming Text using prompts, role-playing and more",
        section_order=3,
        pages=[
            # Everything is a remix: Transformations with contract clauses
            Page(
                title="Everything is a Remix: Transforming contract clauses with LLMs",
                page_order=0,
                path="content/pages/everything_is_a_remix.py",
                beta=True,
            ),
        ],
    ),
]


def convert_section_for_routes(section: Section):
    def convert_page(page: Page) -> st.Page:
        title = f"{'[BETA] ' if page.beta else ''}{page.title}: Prompt Engineering for Lawyers"
        return st.Page(
            page.path,
            title=title,
        )

    section.pages.sort(key=lambda x: x.page_order)

    return {
        section.title: [convert_page(page) for page in section.pages if page.active]
    }


def get_routes():
    result = {
        "": [
            st.Page("content/pages/Home.py", title="Home: Prompt Engineering for Lawyers", default=True, icon="🏠"),
        ]
    }

    data_pages.sort(key=lambda x: x.section_order)

    for section in data_pages[1:]:
        result.update(convert_section_for_routes(section))

    return result


def get_navigation():
    with st.expander("Contents", expanded=True, icon="📚"):
        st.page_link("content/pages/Home.py", label="Home", icon="🏠")
        for section in data_pages[1:]:
            st.caption(section.title)
            for page in section.pages:
                if page.active:
                    if st.session_state["logged_in"]:
                        locked = ":green[:material/lock:]" if page.locked else ":green[:material/lock_open:]"
                    else:
                        locked = f":red[:material/lock:]" if page.locked else ":violet[:material/lock_open:]"

                    label=(f"{locked}"
                           f"{'🚧' if page.beta else ''}"
                           f" {page.title}")
                    st.page_link(page.path, label=label)


def get_routes_list() -> list[Page]:
    return [page for section in data_pages for page in section.pages]
