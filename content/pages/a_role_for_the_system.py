import streamlit as st

# A page template to keep track of all the helper functions and classes that are used in the project.
# Make a copy of this page to begin a new page
from helpers import navigation_footer, check_openai_key, write_what_you_will_learn, write_more_resources
from prompt_widget import chat_prompt

# Page path is used to identify the page in the navigation footer. Use the file path to the page.
PAGE_PATH = "content/pages/a_role_for_the_system.py"

# If this page has exercises, use the check_openai_key() function to check if the user has an OpenAI key.
# Remove this if it is an essay.
check_openai_key()

# Title of the page
st.title("A role for the System")

# A widget to summarise what you will learn on this page
write_what_you_will_learn([
    "Understand the System Role and how it impacts the output of language models",
    "Explore a System Prompt and how it can be used to guide the output of language models",
    "Discover the benefits of using System messages over user messages",
    "Observe real-life examples of System messages and their usage",
    "Learn how to write effective System messages to guide language models",
    "Understand the importance of clear and concise System messages",
])

st.header("The System Role", divider=True)
"""
So far, the way we have interacted with an LLM is by providing a prompt and getting a completion. 
Even during a chat interface, we have only interacted between a user and an assistant. 
However, as in real life, there can be more than two parties involved in a conversation.

For chatbots, a third party is often introduced in the conversation --  the "System" role.
In most cases, the System role is hidden from the user. In this section, we will explore the System role and how it
impacts the output of language models.
"""

st.header("Improving our LLM Note taker?", divider=True)
"""
To understand the System role, let's improve on the LLM Note taker featured 
[in the "Chat as Memory" section](/chat_as_memory#taking-notes-as-a-chat).

We will make one change to it. Can you find it?
"""

exercise = "Welcome our new overlords - the System Role"
chat_prompt(exercise, history=[
    {"role": "system", "content": 'You are an expert note taker for a mediation. Say "OK" to all my notes '
                                  'until the mediation is over. '
                                 'Then produce a narrative summary of the mediation'},
], steps=[
    '9:30am. Supreme Court Meeting Room 1. Mediator - Mr Lee. \n\n'
    'Plaintiff Space Renovations Private Limited. Mr Sashi for the Plaintiff. '
    'Defendant Mr Tan. Mr Vinod for the Defendant.',
    "Mr Lee: [Standard mediator's opening statement] \n\n"
    "We will start by having Plaintiff's Opening Statement. \n\n"
    "Sashi: Renovation contract. Client completed all works under contract and delivered to Tan already. \n\n"
    " Now owed balance $200K under contract. Tan refuse to pay. If not paid, cash flow difficulties, cannot pay "
    "subcontractors. No choice but to bring action against Tan. \n\n"
    "Vinod: Some work was done but it was shoddy and full of defects. "
    "Client had no choice but to accept because baby was about to born.",
    "Vinod cotd: Will not pay unless all defects are fixed",
    "Mr Lee: We will now have caucus with Mr Tan. \n\n [Caucus] \n\n "
    "Mr Lee: Unreasonable to not pay when you have accepted delivery. What can we do to close gap? \n\n"
    " Tan: My family suffered a lot. Roof leaking, water pipes not fixed. They say they delivered but they were "
    "still sending workmen in the house. Baby cannot sleep. Not that we cannot pay, but we feel they disrespected us "
    "and not paying on principle. \n\n"
    "Mr Lee: Apology? \n\n "
    "Tan: OK, but I still want some reduction in contract price because they were late anyway. \n\n "
    "[End caucus with defendant]",
    "[Caucus with Plaintiff]",
    "[Parties return for joint session] \n\n "
    "M: Progress. \n\n "
    "Thank Tan for accepting principle that payment should be made."
    " In fact, Plaintiff didn't realise work was still ongoing and workers created inconvenience for you. "
    "Apology + 5K discount on balance \n\n "
    "Tan: I want 20K \n\n "
    "Plaintiff: 10K is the highest. \n\n Tan: Accepted. \n\n [Draft and sign settlement]",
    "The mediation is over."
])

"""
The first change you must notice is that the chat starts very differently. There is now a new message that
isn't from the user or the assistant. It is in fact the System role.

To put it simply, the system role is a special kind of message used to guide the conversation. In this example,
we told the LLM what to do when receiving our notes (just answer "OK") and what to do when the mediation is over
(produce a narrative summary).

An eagle eyed observer will note that we could have done the exact same thing as the system message did by just 
having the user inform the LLM what it should do. However, I would suggest that there are improvements:

* It is a clear signal to the LLM that the system message is different from the user message. 
It might be unclear how much differently an LLM treats a system message compared to the user message in practice,
but treating system messages which come from the developers differently from user generated messages is useful
from a safety perspective.
* The user experience offered is different. Rather than having the user tell the LLM what to do, we can guide 
the LLM from the the start. In essence, we transformed our LLM to a note taking chatbot.
* We can treat system messages differently. For example, we can hide our instructions to a LLM from the user. 
This is useful when the user doesn't need to know the instructions given to a LLM. A person reading your prompt
in code will also know that the instructions to a LLM are found in the system message. 

If it makes sense to write a system message, it's a good habit to provide them. 
"""

st.header("System Messages in _Real Life_", divider=True)
"""
To write good system messages and understand how to use them effectively, it pays to observe how they are used in
real life. Some may expect such messages to be "secret sauce", but some vendors do provide them for reference. 

In this section, we will be looking at the one Anthropic uses for its 
[Claude 3 Haiku chatbot on 12 July 2024.](https://docs.anthropic.com/en/release-notes/system-prompts) 

>The assistant is Claude, created by Anthropic. The current date is {}. 
>Claude’s knowledge base was last updated in August 2023 and it answers user questions about events 
>before August 2023 and after August 2023 the same way a highly informed individual from August 2023 would 
>if they were talking to someone from {}. 
>It should give concise responses to very simple questions, but provide thorough responses to more complex and 
>open-ended questions. It is happy to help with writing, analysis, question answering, math, coding, and all 
>sorts of other tasks. It uses markdown for coding. It does not mention this information about itself unless the 
>information is directly pertinent to the human’s query.

Here's a list of things which this system message does:
* It provides a summary of what the chatbot is and what it can do ("happy to help with writing, analysis, question
answering, math, coding, and all sorts of other tasks")
* It provides a summary of what the chatbot knows by providing a date and the date which the chatbot's knowledge
was last updated.
* It provides information on how the chatbot should respond ("concise responses to very simple questions")
* It guides the chatbot on how to respond in different scenarios ("provide thorough responses to more complex 
and open-ended questions", coding in "markdown")
* It provides information on what the chatbot should not do ("It does not mention this information about itself")

As you can see, clear and concise system messages can help guide the LLM to provide the output you want.
With experience, you can resolve issues with the LLM output by providing better system messages and continuously
improving on them.
"""

write_more_resources([
    "[Anthropic suggest that giving a role in a system prompt can improve its performance]"
    "(https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/system-prompts#legal-contract-analysis-with-role-prompting)",
    "OpenAI devotes far less space to [system prompts](https://platform.openai.com/docs/guides/prompt-engineering/tactic-ask-the-model-to-adopt-a-persona) "
    "these days. There are observations that the [system prompt effect wears off after a while](https://community.openai.com/t/the-system-role-how-it-influences-the-chat-behavior/87353).",
])

st.header("Conclusion", divider=True)
"""
In this section, we expanded our understanding of the text or chat completion capabilities of LLMs by introducing 
new roles to messages. The System role is a special kind of message used to guide the conversation.

I also hope that broadening your perspective beyond the user and assistant interactions will help you to see that
a lot of the magic in LLMs may be behind the scenes and hidden in system prompts. With some simple adjustments,
we are able to transform the output of an LLM without highlighting it to the user. We did all of this with prompt 
engineering.
"""

# Navigation footer is a common footer that is used in all pages. It provides links to the previous and next pages.
navigation_footer(PAGE_PATH)
