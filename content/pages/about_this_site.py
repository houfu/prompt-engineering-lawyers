import streamlit as st

from helpers import write_essay_page, navigation_footer

PAGE_PATH = "content/pages/about_this_site.py"

write_essay_page()

st.title("About this site")

st.header("What's this? :open_mouth:", divider=True)

"""
It's a course to explore what prompt engineering is and its possibilities. 
At the end of the course, you will:

* Craft prompts that are clear, concise and effective in generating the response you want
* Discover new ways to make large language models work harder for you
* Evaluate the quality of the generated text
* Understand better how to effectively use large language models like ChatGPT, GPT4, Claude, 
Bard, PaLM and many others through prompt engineering.

This course is also focused on **application**. 
It is designed for lawyers and other professionals who want to use prompt engineering in the legal domain. 
The examples and the tasks are focused on the legal domain.

"""

st.header("Why should I take this course? :thinking_face:", divider=True)

"""
If you are a lawyer, and you want to stay ahead of the curve in the ever-evolving world of legal technology,
this is a great way to learn about prompt engineering. (Impress your colleagues!)

If you are not a lawyer, but you want to know how prompt engineering and large language models can affect
legal work, this is a good way to gain exposure.

One of the most important features I wanted is the ability to *experiment*. The widgets in this course
allow a user to input any prompt, so you can follow the course, experiment with your own input or 
compare prompts.

Let's have fun! :the_horns:
"""

st.header("Why do I need to subscribe to this site? :moneybag:", divider=True)

"""
This is not a book or a video. It's an interactive course which allows you to try and apply what you will learn to 
a LLM. 

Behind the scenes, there is a lot of code that makes this course work. This also includes researching and experimenting
to design a lesson which brings out the best in prompt engineering.

While the first iteration of this course was free, I have now decided to make it a paid course. It's a way to motivate
myself to keep improving the course and to keep adding new content. 

It's important to note that subscribing is _not necessary_ to access the course.
There are free pages (marked ":violet[:material/lock_open:]") that you can access without subscribing. 
Some of the more advanced exercises (marked ":red[:material/lock:]") will require a subscription. 
After trying out the free pages, you can decide if you want to subscribe to access the full course.
If you have absolutely no intention of paying anything and the willpower to resist, 
[the source code is available on GitHub](https://github.com/houfu/prompt-engineering-lawyers) 
and with some effort, you can run it on your own computer.
"""

with st.expander("What do I get with a subscription? :key:", expanded=False):
    """
* Access to the full "Prompt Engineering for Lawyers" site
* Be informed of new pages, exercises and updates to the site
* Exclusive content on prompt engineering for subscribers (2-4 times a month)
* Support me to maintain and developing the site
    """

"""

Once you get full access, you will be able to access all the exercises in the site. 
With full access, you will also get access to updates and new exercises that I will be adding in the future.

Ready to get started? :rocket:
"""

st.page_link(
    "https://buymeacoffee.com/houfu/membership",
    label="**Subscribe to this site**",
    icon="👉",
)

st.header("What do I need to use this site? :computer:", divider=True)
"""
**You need an OpenAI API key to use the exercises in this site.**

The key is used to power the examples and exercises throughout the course.
There are several LLMs you can practice and demonstrate prompt engineering on, but OpenAI is the most popular one.

Just a quick heads up that you will incur charges on your OpenAI account when you use the examples and 
exercises in this course. However, don't worry too much, as it will take a lot of queries before you have to pay a 
significant amount of money. 
As of the time of writing, using GPT-4o mini, which is the main LLM we will use on this site, 
1,000 input tokens costs \\$0.000150 and 1,000 output tokens costs \\$0.000600.

As Theodore Roosevelt once said, "The only way to learn anything is to do it." 
So, don't be afraid to experiment and try new things. The more you use the examples and exercises, 
the better you will become at prompt engineering.

If you don't have an OpenAI Key, sign up [here](https://platform.openai.com/signup). Once you have verified
your account, you can generate an API key. You can find more 
[detailed instructions](https://www.howtogeek.com/885918/how-to-get-an-openai-api-key/) here. 

(If you really want to use your favourite LLM, let me know and I may introduce more options in the future.)
"""
navigation_footer(PAGE_PATH)
