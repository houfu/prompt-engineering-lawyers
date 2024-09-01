import streamlit as st

# A page template to keep track of all the helper functions and classes that are used in the project.
# Make a copy of this page to begin a new page
from helpers import navigation_footer, check_openai_key, write_what_you_will_learn
from prompt_widget import simple_prompt

# Page path is used to identify the page in the navigation footer. Use the file path to the page.
PAGE_PATH = "content/pages/now_this.py"

# If you want to write an essay, use the write_essay_page() function.
# It highlights to users of pages that are essays.
# write_essay_page()

# If this page has exercises, use the check_openai_key() function to check if the user has an OpenAI key.
# This allows the user to use OpenAI's GPT-3 API to complete exercises.
# Remove this if it is an essay.
check_openai_key()

# Title of the page
st.title("Now this! Transforming text using LLMs.")

write_what_you_will_learn([
   "Use prompts to transform text in a legal context",
    "Rewrite an email to get the tone you want",
])

"""
One of the easiest and effective ways to use a large language model is to transform a text you have using prompts.

By providing the model with a starting point, such as a sentence or a paragraph, 
we can use prompts to guide the language model towards generating new and original content 
that is closely related to the original input. 
This can be done for a wide range of tasks, such as summarization, paraphrasing, translation, and more.

In the previous section, we provided a simple template you can use to develop your own prompts.
The _context_ of the prompt is the original text, or the text you want to transform.
The _instruction_ tells the LLM what you want to do with it.
It's magic! :sparkles:
"""

exercise_1 = "Rewrite an email to get the tone you want."
st.header(exercise_1)

"""
Lawyers email clients a lot. Clients want updates faster and faster, but lawyers suffer from being human. 
They might be too tired to write an email that sounds professional. 
Here a LLM can "correct" the tone of the email to be more professional.
"""

simple_prompt(exercise_1, default_text="I am a lawyer writing an email to my client. This is my email: "
              "Hey I just wanted to tell you that I went to court today and man the wait was so long. "
              "When I finally got to speak to the Judge, he was like are you all ready for trial? "
              "I told him you still had to make a few more discovery application, "
              "and my learned friend from the other side was like seriously they had a window to do this. "
              "I vigorously argued for an extension of time. It was granted but you have to pay costs. "
              "So now, you have to file your application in two weeks. Next appointment with the judge, in four weeks. "
              "Let me know if you have any questions!  \n\n Rewrite my email in a more professional manner.")

"""
You might be surprised that the LLM was able to fix grammar errors, get rid of colloquialisms and produce a fairly
decent email. 

Here's a follow up exercise for you to practice writing the context and instruction. If you can, a whole new adventure
awaits you! Ask the LLM to do the following instead of writing in a professional tone.

* Write the email in a form of a haiku
* Write the email in the voice of a pirate lawyer
* Write the email in Singlish (or whatever local dialect you can think of).

You will note that the LLM can transform the text significantly, making it longer or shorter. However,
by instructing the LLM to rewrite your passage, you can get a new text that isn't too different from your original,
whether by adding new sections or removing its main points.
When you experiment with more prompts though, you will find that there are some instances 
that can miss the mark or a nuance.
"""


st.header("Conclusion")

"""
In conclusion, the use of LLMs in law offers opportunities to transform and simplify text through effective prompts. 
While LLMs can improve language, they have limitations due to their general training and the need for human expertise. 
Rewriting contract clauses with LLMs can enhance accessibility, but legal advice remains essential. 
Harnessing LLMs requires a discerning approach, balancing their potential with human knowledge and
 ethical considerations. LLMs are powerful tools to enhance efficiency and accessibility in the legal field. 

"""

# Navigation footer is a common footer that is used in all pages. It provides links to the previous and next pages.
navigation_footer(PAGE_PATH)
