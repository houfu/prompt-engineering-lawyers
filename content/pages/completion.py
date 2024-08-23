import streamlit as st

# A page template to keep track of all the helper functions and classes that are used in the project.
# Make a copy of this page to begin a new page
from helpers import navigation_footer, check_openai_key, write_what_you_will_learn, write_more_resources
from prompt_widget import simple_prompt

# Page path is used to identify the page in the navigation footer. Use the file path to the page.
PAGE_PATH = "content/pages/completion.py"

# If this page has exercises, use the check_openai_key() function to check if the user has an OpenAI key.
# This allows the user to use OpenAI's GPT-3 API to complete exercises.
# Remove this if it is an essay.
check_openai_key()

# Title of the page
st.title("From Prompt to Completion")

write_what_you_will_learn([
    "Try out the completion interface which we will be using throughout the course",
    "Get used to querying the LLM and evaluating the output",
    "The randomness of LLMs",
])

st.header("The basic interface of LLMs", divider=True)
"""
Many people experience the power of LLMs in various guises, such as chatbots or search engines.

When you get down to its essence,
the basic interface of large language models (LLMs) is simple. You provide a prompt and the LLM generates text. 
The input is the prompt, and the output is the completion.
It's called a completion because the LLM "completes" the prompt by predicting the next words in the sequence.

Let's focus on getting you used to the basic experience of interacting with an LLM.
Hopefully, you will get a chance to familiarise yourself with the basic tools of this course and
get used to writing prompts, getting feedback from the LLM and evaluating the output. 
"""

st.header("Let's Throw Something at a LLM", divider=True)
"""
Let's ask the LLM a simple question. In the exercise area below, I have already provided the prompt to try. 
"""

simple_prompt("Let's Throw Something at a LLM", default_text="What is will in ten words or less?")

"""

1. Click submit and wait for the LLM to give a response.

2. Now, ask the LLM again. Did you get the same response? 

3. Assume you were aiming for the meaning of will as a testamentary disposition. 
Did you get that meaning? Even after several tries?

4. Notice that we did put a constraint on the response by specifying a limit on the number of words. Now remove that
constraint, and see if the LLM gives you a better response. 
You probably did reach your aim this time, but you probably got a list of meanings. 
This is great, unless you were only aiming for one meaning.

5. Now, ask the LLM again (without the word limit) and see if you get the same response. 
Broadly speaking, you might get the same response, but the LLM always uses different words to define the same concept.
"""

st.header("Your first lesson on LLMs: Randomness", divider=True)
"""
Understandably, most people focus on what LLMs can "do". But if you want to understand LLMs and use them effectively,
you need to grapple with their randomness.

Randomness causes the LLM to give different responses to the same prompt. It causes hallucinations, bugs, dangerous
responses and many other problems.

However, it is also its singular power. It allows the LLM to generate text that is creative, surprising and sometimes
even useful.

Your task as a prompt engineer is to find a balance between randomness and control.
"""

write_more_resources(
    [
        "[An explanation on how LLMs work from Stephen Wolfram (with lots of graphs, diagrams and math"
        "s)](https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/)",
    ]
)

# Navigation footer is a common footer that is used in all pages. It provides links to the previous and next pages.
navigation_footer(PAGE_PATH)
