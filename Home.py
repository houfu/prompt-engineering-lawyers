import streamlit as st
from streamlit_url_fragments import get_fragments

from auth_helpers import welcome_mat
from helpers import use_custom_css, write_footer, is_supabase_session_params

st.set_page_config(
    page_title="Home — Prompt Engineering for Lawyers",
    layout="wide"
)


if 'supabase_session' not in st.session_state:
    session_params = get_fragments()
    st.session_state['supabase_session'] = session_params if is_supabase_session_params(session_params) else None


if 'api_success' not in st.session_state:
    st.session_state['api_success'] = False

use_custom_css()

st.title("Prompt Engineering for Lawyers")

welcome_mat()

st.header("What's this? :open_mouth:")

"""
It's a course to explore what prompt engineering is and its possibilities. 
At the end of the course, you will:
 
* Craft prompts that are clear, concise and effective in generating the response you want
* Discover new ways to make large language models work harder for you
* Evaluate the quality of the generated text
* Understand better how to effectively use large language models like ChatGPT, GPT4, Claude, 
Bard, PaLM and many others through prompt engineering.

This course is also focused on **application**. 
It is designed for lawyers and other professionals who want to use prompt engineering in a variety of tasks in the 
legal domain. 
The examples and the tasks are focused on the legal domain.

"""

st.header("Why should I take this course? :thinking_face:")

"""
If you are a lawyer, and you want to stay ahead of the curve in the ever-evolving world of legal technology,
this is a great way to learn about prompt engineering. (Impress your colleagues!)

If you are not a lawyer, but you want to know how prompt engineering and large language models can affect
legal work, this is a good way to gain exposure.

One of the most important features I wanted is the ability to *experiment*. The widgets in this course
allow a user to input any prompt, so you can follow the course, experiment with your own input or 
compare two prompts to compare how effective they are.

Let's have fun! :the_horns:
"""


write_footer()
