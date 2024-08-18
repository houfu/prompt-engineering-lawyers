import streamlit as st

# A page template to keep track of all the helper functions and classes that are used in the project.
# Make a copy of this page to begin a new page
from helpers import navigation_footer, write_essay_page

# Page path is used to identify the page in the navigation footer. Use the file path to the page.
PAGE_PATH = "content/pages/what_is_prompt_engineering.py"

# If you want to write an essay, use the write_essay_page() function.
# It highlights to users of pages that are essays.
write_essay_page()

# Title of the page
st.title("What is Prompt Engineering?")

"""
It's strange that despite two years since the introduction of GPT-3 
(which quickly brought forth the concept of prompt engineering), 
there is still no clear definition of what prompt engineering is.

Here are some definitions that I have come across:
* _Prompt engineering is the process of structuring an instruction that can be interpreted and 
understood by a generative AI model. A prompt is natural language text describing the task that an AI should perform._
: [Wikipedia](https://en.wikipedia.org/wiki/Prompt_engineering)
* _Prompt engineering is the practice of designing inputs for AI tools that will produce optimal outputs._
: [McKinsey](https://www.mckinsey.com/featured-insights/mckinsey-explainers/what-is-prompt-engineering)
* _Prompt engineering is a relatively new discipline for developing and optimizing prompts to 
efficiently use language models (LMs) for a wide variety of applications and research topics._ 
: [Prompt Engineering Guide](https://www.promptingguide.ai/)

So to sum up, prompt engineering is the process of designing prompts that will generate the desired output from 
a language model.
"""

st.header("Why is prompt engineering important?")
"""
To be fair, every time you use a large language model, you are doing prompt engineering.
One of the best features of large language models is their ability to generate text based on a prompt using natural
language instead of, for example, a programming language. This removes a potential barrier to using AI. 
"""

# Navigation footer is a common footer that is used in all pages. It provides links to the previous and next pages.
navigation_footer(PAGE_PATH)