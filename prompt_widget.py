from typing import Literal

import streamlit as st

EXERCISE_TYPES = ['simple_prompt', 'chat']

MODEL = Literal['gpt-3.5-turbo', 'gpt-4']


def exercise_area(title="Exercise", exercise_type: EXERCISE_TYPES = 'simple_prompt', **kwargs):
    if st.session_state.get("api_success", False) is False:
        return st.error("""
        This exercise will not be loaded as no OpenAI key was found.
        
        Click Home in the Sidebar, enter your API Key and return here.
        """, icon="🤦‍♀️")
    content_key = f"exercise-area-{title}-content"

    if content_key not in st.session_state:
        st.session_state[content_key] = []

    if exercise_type == 'chat':
        pass
    else:
        return simple_prompt(content_key, title, **kwargs)


def simple_prompt(content_key, title, **kwargs):
    default_text = kwargs['default_text'] if 'default_text' in kwargs else ''
    long = kwargs['long'] if 'long' in kwargs else True
    model: MODEL = kwargs['model'] if 'model' in kwargs else 'gpt-3.5-turbo'

    exercise_container = st.container()
    exercise_container.divider()
    with exercise_container.form(f"exercise-area-{title}"):
        prompt = st.text_area(
            value=default_text,
            label="Prompt",
            height=550 if long else 180
        )
        submitted = st.form_submit_button("Submit")
        if model == "gpt-4":
            model_name = "GPT-4"
        else:
            model_name = "ChatGPT"
        if submitted:
            with st.spinner(f"Now asking {model_name}."):
                import openai
                response = openai.ChatCompletion.create(
                    model=model,
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
            f"☝️ Input your prompt and click the submit the button to generate the text from {model_name}.")
    exercise_container.divider()
    return exercise_container
