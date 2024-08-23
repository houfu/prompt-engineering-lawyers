import datetime
from typing import Optional

import openai
import streamlit as st
from pydantic import BaseModel


def check_openai_key():
    if st.session_state.get("openai_key", None) is None:
        st.error(
            """
        This exercise will not be loaded as no OpenAI key was found.

        Enter your API Key in the box at the top of this page and return here.
        """,
            icon="🤦‍♀️",
        )
        return True
    return False


class SimplePromptHistoryItem(BaseModel):
    user: str
    assistant: Optional[str] = None
    date: datetime.datetime = datetime.datetime.now()




def simple_prompt(title, **kwargs):
    default_text = kwargs["default_text"] if "default_text" in kwargs else ""
    long = kwargs["long"] if "long" in kwargs else True

    if check_openai_key():
        return

    content_key = f"exercise-area-{title}-content"
    history_key = f"exercise-area-{title}-history"

    if content_key not in st.session_state:
        st.session_state[content_key] = []

    if history_key not in st.session_state:
        st.session_state[history_key] = (
            len(st.session_state[content_key])
            if len(st.session_state[content_key]) > 0
            else 1
        )

    exercise_container = st.container(border=True)
    exercise_container.header(f"Exercise: {title}")
    with exercise_container.form(key=f"{content_key}-form"):
        prompt = st.text_area(
            "Prompt",
            default_text,
            key=f"{content_key}-prompt",
            height=200 if long else 100,
        )
        submitted = st.form_submit_button("Submit")

        if submitted:
            st.session_state[content_key].append(SimplePromptHistoryItem(user=prompt))
            st.session_state[history_key] = len(st.session_state[content_key])

    with exercise_container:
        if len(st.session_state[content_key]) > 0:
            current_history_item = st.session_state[content_key][
                st.session_state[history_key] - 1
            ]
            with st.chat_message("user"):
                st.caption(f"On {current_history_item.date.strftime('%B %d, %Y at %I:%M%p')}")
                st.write(current_history_item.user)

            if current_history_item.assistant:
                st.chat_message("assistant").write(current_history_item.assistant)
            else:

                client = openai.Client(api_key=st.session_state.openai_key)

                with st.chat_message("assistant"):
                    stream = client.chat.completions.create(
                        model="gpt-4o-mini",
                        messages=[{"role": "user", "content": prompt}],
                        stream=True,
                    )
                    response = st.write_stream(stream)

                current_history_item.assistant = response

                st.session_state[content_key][
                    st.session_state[history_key] - 1
                ] = current_history_item

        def update_history_key():
            st.session_state[history_key] = st.session_state[f"exercise-area-{title}-slider"]

        if len(st.session_state[content_key]) > 1:
            st.slider(
                "History",
                1,
                len(st.session_state[content_key]),
                st.session_state[history_key],
                key=f"exercise-area-{title}-slider",
                on_change=update_history_key,
            )

    return exercise_container
