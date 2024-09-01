import streamlit as st

# A page template to keep track of all the helper functions and classes that are used in the project.
# Make a copy of this page to begin a new page
from helpers import navigation_footer, check_openai_key, write_what_you_will_learn
from prompt_widget import chat_prompt

# Page path is used to identify the page in the navigation footer. Use the file path to the page.
PAGE_PATH = "content/pages/chat_as_memory.py"

# If this page has exercises, use the check_openai_key() function to check if the user has an OpenAI key.
# Remove this if it is an essay.
check_openai_key()

# Title of the page
st.title("Chat as Memory")

# A widget to summarise what you will learn on this page
write_what_you_will_learn([
    "Introducing the chat interface",
    "Understand the usefulness of a chat history as a simple storage mechanism",
    "Take notes during a court hearing and enhance them using a LLM",
    "Explore the differences between chat and completion interfaces",
    "Understand the role of context in chat interfaces",
    "Understand the potential of prompt engineering in chat interfaces for lawyers"
])

st.header("Why is everything a chatbot?", divider=True)

"""
In the previous exercises, we have been using the completion interface to interact with the LLM. 
While it is necessary to understand completion to understand how an LLM works, it is not the usual way we interact with
LLMs.

In fact, if you asked most people about LLMs, they would almost always associate them with chatbots.
Chatbots do provide a user experience that favours LLM's natural language understanding and generation capabilities,
however in the next few sections we will explore other aspects of a chat which enhance the capabilities of a LLM.  
"""

exercise_3 = "Who's Bob?"
st.header(f'{exercise_3}')
"""
This will be our first interaction with the chat interface in this course. For educational purposes,
some aspects of the chat interface may not be in line with the usual chat interface you are familiar with.

For example, there's already some messages in the chat and I've already provided you with a prompt to put in.
Try entering it. You will notice that after you submit your response, the chat will provide you with the next
step to take. Following this allows you to complete the exercise, even though you are not compelled to do so.
"""

chat_prompt(exercise_3, history=[
    {"role": "assistant", "content": "I'm Bob, an innovative lawyer here to help you understand LLMs."}
], steps=[
    "Glad to meet you. What can you tell me about LLMs in 20 words or less?",
    "Sorry, what's your name?"
])

"""
At the end of the chat, you will be asked to query the assistant on its name. The assistant answers it correctly - Bob.

This wouldn't be possible in the completion interface as the LLM doesn't have any record of previous interactions.
You can probably tell what is happening here. The chat stores the history of the conversation, and the LLM uses it
as _context_ to complete the response.

The chat interface also provides a way to reset your conversation and to browse previous chats, which are similar
to the completion interface. You can take some time to get used to the chat interface.
"""

st.info("If you have read the code repository to this course (A link can be found at the bottom of this page), "
        "you will find that both the prompt and the chat exercise areas use the same command to generate output. "
        "Most lawyers will now claim that '_Equity looks to the intent, rather than to the form_.' "
        "It's easy to format a prompt in the form of the chat, so don't make too much effort to distinguish them.",
        icon="😛")

st.header("Taking notes as a chat", divider=True)
"""
When attending hearings or meetings, many lawyers stick to pen or paper, 
or use some word processing software or note-taking software to take down notes. 
As they are taken down quickly, they often messy and hard to read.

Chat applications don't look like they should be used for note taking. 
(They are conversations, right?) 
However, when combined with a large language model, you can find new and surprising uses.
"""

exercise_4 = "The fly on the wall during a mediation"
chat_prompt(exercise_4, history=[
    {"role": "user", "content": 'I am a lawyer and I am taking down notes by telling you what is going on during '
                                 'my mediation. Say "OK" to all my notes until the mediation is over. '
                                 'Do you understand?.'},
    {"role": "assistant", "content": 'Yes, I understand. Please proceed.'}
], steps=[
    '9:30am. Supreme Court Meeting Room 1. Mediator - Mr Lee. \n\n'
    'Plaintiff Space Renovations Private Limited. Mr Sashi for the Plaintiff. '
    'Defendant Mr Tan. Mr Vinod for the Defendant.',
    "Mr Lee: [Standard mediator's opening statement] \n\n"
    "We will start by having Plaintifff's Opening Statement. \n\n"
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
    "The mediation is over. Now generate a narrative summary of the mediation."
])

"""
Were you satisfied with the summary provided by the LLM?
You would notice that the LLM was able to access events that happened earlier in the message history and use
them to generate a narrative summary of the mediation.

Interestingly, you would notice that the LLM was able to generate  summary of the mediation, even when
there are short forms, spelling errors and even possible industry terms you may not expect the LLM to be familiar with.
"""

st.header("Conclusion", divider=True)
"""
In this section, we discovered the power of prompt engineering for lawyers using chat interfaces. 
By treating chat as a data storage tool, we can expand the capabilities of LLMs, by for example, taking notes using
burst of information taken in real time.

In the next section, we will expand on the idea of chat to introduce another concept which makes LLMs more powerful. 
"""

navigation_footer(PAGE_PATH)
