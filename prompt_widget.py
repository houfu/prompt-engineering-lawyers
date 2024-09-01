import datetime
from typing import Optional, Literal, TypedDict, List, Union

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
    exercise_container.subheader(f"Exercise: {title}")
    with exercise_container.form(key=f"{content_key}-form"):
        prompt = st.text_area(
            "Prompt",
            default_text,
            key=f"{content_key}-prompt",
            height=500 if long else None,
        )
        submitted = st.form_submit_button("Submit", type="primary")

        if submitted:
            st.session_state[content_key].append(SimplePromptHistoryItem(user=prompt))
            st.session_state[history_key] = len(st.session_state[content_key])

    with exercise_container:
        if len(st.session_state[content_key]) > 0:
            current_history_item = st.session_state[content_key][
                st.session_state[history_key] - 1
            ]
            with st.chat_message("user"):
                st.caption(
                    f"On {current_history_item.date.strftime('%B %d, %Y at %I:%M%p')}"
                )
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
            st.session_state[history_key] = st.session_state[
                f"exercise-area-{title}-slider"
            ]

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


CHAT_PROMPT_ROLE = Literal["user", "assistant", "system"]


class ChatPromptMessage(TypedDict):
    role: CHAT_PROMPT_ROLE
    content: str


def chat_prompt(title: str, **kwargs):
    history: List[ChatPromptMessage] = kwargs.get("history", [])
    steps: Union[List[str]] = kwargs.get("steps", [])
    long = kwargs.get("long", False)

    if not isinstance(history, list) or not all(
        isinstance(item, dict) and "role" in item and "content" in item
        for item in history
    ):
        raise TypeError("history must be a list of ChatPromptMessage objects")

    if not isinstance(steps, list) or not all(isinstance(item, str) for item in steps):
        raise TypeError("steps must be a list of strings")

    if check_openai_key():
        return

    # Initialize

    content_key = f"exercise-area-{title}-content"
    history_key = f"exercise-area-{title}-history"
    steps_key = f"exercise-area-{title}-steps"

    if content_key not in st.session_state:
        st.session_state[content_key] = []
        st.session_state[content_key].append(history)

    if history_key not in st.session_state:
        st.session_state[history_key] = 1

    if steps_key not in st.session_state:
        st.session_state[steps_key] = [0]

    # Set messages to correct history

    messages = st.session_state[content_key][st.session_state[history_key] - 1]

    # Create exercise container
    exercise_container = st.container(border=True)
    exercise_container.subheader(f"Exercise: {title}")

    # Produce conversation history in container
    conversation = exercise_container.container()

    with conversation:
        for message in messages:
            with st.chat_message(message["role"]):
                st.write(message["content"])

    # Create form area
    def get_form_area(prompt=None):
        with st.form(key=f"{content_key}-form", clear_on_submit=True):

            step_area = st.empty()

            prompt = st.text_area(
                "Prompt",
                prompt if prompt else "",
                key=f"{content_key}-prompt",
                height=500 if long else None,
            )

            if (
                len(steps) > 0
                and st.session_state[steps_key][st.session_state[history_key] - 1] == 0
            ):
                with step_area.container():
                    st.caption(f"Prompt for this step:")
                    st.chat_message("user").write(steps[0])

            def update_step():
                if len(steps) > 0:
                    step_text = (
                        steps[
                            st.session_state[steps_key][
                                st.session_state[history_key] - 1
                            ]
                        ]
                        if st.session_state[steps_key][
                            st.session_state[history_key] - 1
                        ]
                        < len(steps)
                        else ""
                    )
                    if step_text:
                        with step_area.container():
                            st.caption(f"Prompt for this step:")
                            st.chat_message("user").write(f"{step_text}")

            submitted = st.form_submit_button("Submit", type="primary")

            if submitted:
                messages.append({"role": "user", "content": prompt})

                if len(steps) > 0:
                    st.session_state[steps_key][st.session_state[history_key] - 1] += 1

                update_step()

                client = openai.Client(api_key=st.session_state.openai_key)

                with conversation:
                    st.chat_message("user").write(prompt)
                    with st.chat_message("assistant"):
                        stream = client.chat.completions.create(
                            model="gpt-4o-mini",
                            messages=messages,
                            stream=True,
                        )
                        response = st.write_stream(stream)

                messages.append({"role": "assistant", "content": response})

                st.session_state[content_key][
                    st.session_state[history_key] - 1
                ] = messages

    form_area = exercise_container.empty()

    with form_area:
        get_form_area()

    col1, col2 = exercise_container.columns([1, 5])
    with col1:
        reset = st.button("Reset", key=f"exercise-area-{title}-reset")

        if reset:
            st.session_state[content_key].append(history)
            st.session_state[history_key] = len(st.session_state[content_key])
            st.session_state[steps_key].append(0)
            st.rerun()

    with col2:

        def update_history_key():
            st.session_state[history_key] = st.session_state[
                f"exercise-area-{title}-slider"
            ]
            st.rerun()

        if len(st.session_state[content_key]) > 1:
            st.slider(
                "History",
                1,
                len(st.session_state[content_key]),
                st.session_state[history_key],
                key=f"exercise-area-{title}-slider",
                on_change=update_history_key,
            )
