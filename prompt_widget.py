from enum import Enum
from typing import Literal

import openai
import streamlit as st
from streamlit_chat import message


class ExerciseType(Enum):
    CHAT = 'chat'
    SIMPLE_PROMPT = 'simple_prompt'


class OpenAIModel(Enum):
    ChatGPT = 'gpt-3.5-turbo'
    GPT4 = 'gpt-4'


def simple_chat(content_key, **kwargs):
    if content_key not in st.session_state:
        st.session_state[content_key] = kwargs['messages'] if 'messages' in kwargs else []
    model: OpenAIModel = kwargs['model'] if 'model' in kwargs else OpenAIModel.ChatGPT
    reset_conversation = False
    clear_form_key = f"{content_key}-clear"
    if clear_form_key not in st.session_state:
        st.session_state[clear_form_key] = False

    if model == OpenAIModel.GPT4:
        try:
            openai.Model.retrieve(model)
        except openai.InvalidRequestError:
            st.error(
                f"Your API Key doesn't have access to {OpenAIModel.GPT4.name}, which is required for this exercise. "
                "The exercise will not load.", icon="😢")

    exercise_container = st.container()
    exercise_container.divider()

    def get_text():
        input_text = st.text_input("You: ", key=f"{content_key}-chat-input")
        return input_text

    def get_avatar(role) -> Literal["pixel-art-neutral", "bottts", "bottts-neutral"]:
        if role == "user":
            return "pixel-art-neutral"
        elif role == "assistant":
            return "bottts"
        else:
            return "bottts-neutral"

    if st.session_state[clear_form_key]:
        st.session_state[f"{content_key}-chat-input"] = ""
        st.session_state[clear_form_key] = False

    for index, content_message in enumerate(st.session_state[content_key]):
        message_role = content_message["role"]
        message(
            content_message["content"],
            is_user=message_role == "user",
            avatar_style=get_avatar(message_role),
            seed=38,
            key=f"{content_key}-{index}"
        )

    user_input = get_text()

    if user_input:
        st.session_state[content_key].append({
            "role": "user",
            "content": user_input
        })

        with st.spinner(f"Now asking {model.name}."):
            response = openai.ChatCompletion.create(
                model=model.value,
                messages=st.session_state[content_key]
            )
            st.session_state[content_key].append({
                "role": "assistant",
                "content": response['choices'][0]['message']['content']
            })

            st.session_state[clear_form_key] = True
            st.experimental_rerun()

    if content_key in st.session_state and len(st.session_state[content_key]) > 0:
        reset_conversation = st.button("Reset conversation", key=f"{content_key}-reset")
    else:
        st.write('Enter some text to start a chat.')

    if reset_conversation:
        st.session_state[content_key] = kwargs['messages'] if 'messages' in kwargs else []
        st.session_state[clear_form_key] = True

    st.divider()

    return exercise_container


def simple_prompt(content_key, title, **kwargs):
    default_text = kwargs['default_text'] if 'default_text' in kwargs else ''
    long = kwargs['long'] if 'long' in kwargs else True
    model: OpenAIModel = kwargs['model'] if 'model' in kwargs else OpenAIModel.ChatGPT

    if content_key not in st.session_state:
        st.session_state[content_key] = []

    exercise_container = st.container()
    exercise_container.divider()
    with exercise_container.form(f"exercise-area-{title}"):
        prompt = st.text_area(
            value=default_text,
            label="Prompt",
            height=550 if long else None,
            max_chars=2500
        )
        submitted = st.form_submit_button("Submit")
        if model == "gpt-4":
            try:
                openai.Model.retrieve(model)
            except openai.InvalidRequestError:
                st.error(f"Your API Key doesn't have access to {model.name}, which is required for this exercise. "
                         "The exercise will not load.", icon="😢")
        if submitted:
            with st.spinner(f"Now asking {model.name}."):
                response = openai.ChatCompletion.create(
                    model=model.value,
                    messages=[
                        {"role": "user", "content": prompt}
                    ]
                )
                content = (prompt, response.choices[0].message.content)
                st.session_state[content_key] += [content]

    if len(st.session_state[content_key]) > 1:
        content_container = exercise_container.container()
        value = exercise_container.slider("Generation index", 1, len(st.session_state[content_key]),
                                          len(st.session_state[content_key]),
                                          label_visibility="collapsed",
                                          key=f"exercise-area-{title}-slider")
        content_container.caption(":green[Generations - use the slider to browse previously generated text]")
        content_container.caption(f"You asked: **{st.session_state[content_key][value - 1][0]}**")
        content_container.write(st.session_state[content_key][value - 1][1])
    elif len(st.session_state[content_key]) > 0:
        exercise_container.write(st.session_state[content_key][0][1])
    else:
        exercise_container.write(
            f"☝️ Input your prompt and click the submit the button to generate the text from {model.name}.")
    exercise_container.divider()
    return exercise_container


def exercise_area(title="Exercise", exercise_type: ExerciseType = ExerciseType.SIMPLE_PROMPT, **kwargs):
    if st.session_state.get("api_success", False) is False:
        return st.error("""
        This exercise will not be loaded as no OpenAI key was found.

        Click Home in the Sidebar, enter your API Key and return here.
        """, icon="🤦‍♀️")
    content_key = f"exercise-area-{title}-content"

    if exercise_type == ExerciseType.CHAT:
        return simple_chat(content_key, **kwargs)
    else:
        return simple_prompt(content_key, title, **kwargs)
