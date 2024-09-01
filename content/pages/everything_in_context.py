import streamlit as st

# A page template to keep track of all the helper functions and classes that are used in the project.
# Make a copy of this page to begin a new page
from helpers import navigation_footer, check_openai_key, write_what_you_will_learn
from prompt_widget import simple_prompt

# Page path is used to identify the page in the navigation footer. Use the file path to the page.
PAGE_PATH = "content/pages/everything_in_context.py"

# If this page has exercises, use the check_openai_key() function to check if the user has an OpenAI key.
# This allows the user to use OpenAI's GPT-3 API to complete exercises.
# Remove this if it is an essay.
check_openai_key()

# Title of the page
st.title("Everything in its Right Context")

write_what_you_will_learn(
    [
        "Explore the concept of context in designing prompts",
        "Understand how context affects the output of language models",
    ]
)

"""
## A simple way to understand the structure of a prompt

In the previous exercise, we asked an LLM to define the word "will". We hoped to get the meaning of a "will"
as a testamentary disposition. However, we got a list of meanings or a different meaning from what we wanted.
Trying repeatedly didn't help.
In most use cases, we want the LLM to give us the meaning we want every time we ask for it. 

A straightforward way to improve this, if a bit glib, is to give it _better instructions_.

Consider the following prompt:
> :red[I am at my lawyer's office.] :green[What is a will?]

The green part of the prompt, plainly, is an instruction or a goal. We tell the LLM what we want, otherwise the LLM
tries to guess what it is supposed to output.

The red part of the prompt is the **context**. It guides the LLM on where it should locate its answers.
The goal here is to get the LLM to give us the meaning of a will as a testamentary disposition, and 
we hope the context will help the LLM to produce more reliable output.

In this section, we will explore the power and limits of providing context to LLMs to get the output we want.
"""

with st.expander("Why don't we just improve the drafting of our goals and instructions instead of context?"):
    """
    OK, so this is the deal. Instead of using context, we could prompt the LLM like this:
    _"Define a will as a testamentary disposition"_. This is a solid instruction, and it works. (Go try it below!)

    However, assuming we can define a goal in such a strict and narrow way, we get into a bit of a pickle.

    If we wanted definitions of a will, isn't it cheaper and faster to use a dictionary?

    We're missing out on the LLM's key feature. A user may not know the exact words to use to get the output they want.
    Heck, they might even not know what they want. It could be rife with typos, or contain unnecessary details.
    Notwithstanding, _understanding the context_, the LLM is able to produce an output which is more likely to be
    what the user wants. And it does succeed too, at times.
    """

st.header("Exercise: Everything in its Right Context", divider=True)

"""
Let's see what happens when we provide or modify the context in the prompt.

We are going to use the prompt we introduced earlier and modify the context in various ways to see how it affects the
output. So follow along! Remember to use the history slider to see the changes in the output.
"""

simple_prompt("Everything in its right context", default_text="I am at my lawyer's office. What is will?")

"""
1. Prompt "I am at my lawyer's office. What is will?": This is the original prompt. You will probably get a law-
related definition of a will. Notice that nobody said anything about what you are doing at the lawyer's office, 
but the context is enough to guide the LLM to give a law-related definition.

2. Prompt "I am outside a law firm. What is will?": The context has changed. You are now outside a law firm. Proximity
wise, you are close to a law firm, but you are not in it. What do you think the LLM will output? What's the logical 
connection between being outside a law firm and a will? Probably not much, but the LLM believes you are looking for
a legal related definition.

3. Prompt "I am at a party. What is will?": You are at a party. What do you think the LLM will output? Probably not 
anything related to a will. Therefore, if you change the context, the output will change as well.

4. Prompt "I am at a party with several geriatrics. What is will?": Now you've managed to steer the LLM to output 
something law related. Good job! With some creativity, you can guide the LLM to give you the output you want.

5. Prompt "It's the year 6123. What is will?": You've changed the context to the future. It's really a nonsensical
request, but the LLM is still able to output meaningful content. I am not as confident as the LLM in predicting 
there would be few changes in meaning of the word within 3000 years.  

Remember to try your own prompts. Do you get the output you were expecting? 
"""

st.header("Conclusion", divider=True)

"""
One of the most oft-repeated advice in prompt engineering is to provide clear context. 
As you can see from the exercise, merely adding a few words can drastically change the output of the LLM.

Throughout this course, we'll be harnessing this power to get the LLM to output the desired results. Now _that's_
prompt engineering.
"""


# Navigation footer is a common footer that is used in all pages. It provides links to the previous and next pages.
navigation_footer(PAGE_PATH)
