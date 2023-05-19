import streamlit as st


from helpers import use_custom_css, check_openai_key, write_footer
from  prompt_widget import exercise_area

st.set_page_config(
    page_title="Let's Begin! — Prompt Engineering for Lawyers",
    layout="wide"
)

use_custom_css()

check_openai_key()

st.title("Let's Begin!")

st.info("""
This section describes what a prompt is and helps you to try using exercise areas. If you're already ready to do some
prompt engineering, you might want to skip to the next section.
""")

st.header("What is a prompt?")

"""
In prompt engineering, a prompt is a piece of text that is used to guide a large language model (LLM) 
to generate a specific output.

Prompts can be as simple as a single word or phrase, or they can be more complex, consisting of multiple sentences 
or even paragraphs. The best prompts are specific, clear, and concise. They should provide the LLM with enough 
information to generate the desired output, but they should not be so specific that they limit the LLM's creativity.

Let's test this out with a simple prompt.
"""

st.subheader("Exercise 1-1: Let's throw something at ChatGPT")

"""
Let's ask ChatGPT a simple question. In the exercise area below, I have already provided the prompt
to try. Click submit and wait for ChatGPT to give a response. 
"""

exercise_area("Exercise 1-1", default_text="What is will?", long=False)

"""
You would probably get an answer like "free will" in a philosophical context.

However, if you wanted the will that takes effect after a testator passes away, you _might_ just get it.
Try clicking submit a few times and see if you can get that meaning. Notice too, that the responses vary a lot! 
"""

st.subheader("Exercise 1-2: Let's aim first instead")

"""
If you wanted the definition of the will that takes effect after a testator passes away, you need to be more
_specific_. That way, you get the definition the first time you ask the LLM. 
(Let's save some API request fees too!)

This time, let's be more specific before firing at ChatGPT.
"""

exercise_area("Exercise 1-2", default_text="What is a will in the legal sense?", long=False)

"""
Now you're going to get the definition of a will in a legal sense, not the philosophical one.

If you click the submit button a few times, you would notice that you are still going to get a variety of answers
(even though they all refer to the will in a legal sense).

You can also get the response you want through different, but similar sounding prompts. Try the following!

* You are a lawyer. What is a will?
* I am in a law office. What is a will?
* I would like to make a will. What is a will?
* You are at a wealth planning conference. What is a will?
* I am at a legal aid clinic. A visitor asked me what is a will. How should I respond?
* A human and his AI assistant go to a bar. The human asked the AI assistant about a will. What is a will?
"""

st.header("More about prompts")

"""
We are early in this course, but I hope you can glean these pros and cons in using prompts.

Pros 👍:
1. Allows you to direct the output of a language model towards a specific topic or theme.
2. Provides a structured approach to generating text, which can be useful for specific applications like chatbots 
or content creation.
3. Can help to save time by providing guidance to the language model, which reduces the amount of trial and error 
required to get the desired output.
4. With the right prompts, language models can generate high-quality text that is similar to human-written content.

Cons 👎:
1. If the prompts are too narrow, it can limit the creativity and variety of the language model's output.
2. Writing effective prompts requires skill and experience, which can take time to develop.
3. There is always some degree of randomness in the output of a language model, even when using prompts.
4. Depending on the complexity of the task, it may be difficult or impossible to generate the desired output 
using prompts alone. 

Overall, while there are some challenges to using prompts, they can be an effective tool for directing the output of 
language models and generating high-quality text. It's important to keep in mind that prompts are not a silver bullet, 
and may need to be combined with other approaches to achieve the desired results. 
"""

st.header("Conclusion")

"""
Let's sum up what we've learned so far. 

In the exercises, you've had a chance to practice prompting ChatGPT with some simple prompts. 
Hopefully, this has helped you get comfortable with the controls we will be using in this course. 

So get ready for the next section where we'll put our new skills to the test by asking ChatGPT to rewrite the text!
"""

write_footer()
