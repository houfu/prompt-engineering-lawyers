import streamlit as st

from helpers import use_custom_css, check_openai_key, write_footer
from prompt_widget import exercise_area

st.set_page_config(
    page_title="Exploring Memory using Chat — Prompt Engineering for Lawyers",
    layout="wide"
)

use_custom_css()

check_openai_key()

st.title("Exploring Memory using Chat")

"""
Most people's first experience with Language Models (LLMs) and generative AI is often through chat interfaces like 
ChatGPT. But what makes chat special? Is it because we can pretend to talk to an AI as if it were a person, 
leading to fears of a Skynet scenario?

I suggest that what makes chat special is that it provides a simple way to access something important to computers: 
memory. When we stop thinking of chat as a conversation with the AI and instead as a data storage tool, we can do 
a lot more with our prompts. 
The possibilities expand greatly, and we can use chat to tap into the full potential of LLMs and generative AI. 
"""

with st.expander("Chat vs. Completion"):
    """
So far, you have seen completion interface. In this exercise, you what use a chat interface. In the context of 
generative AI, the terms "chat" and "completion" refer to different modes of interaction and usage.

Chat: Chat-based models are designed to simulate conversational agents. 
They are trained to understand and generate human-like responses in a conversational manner. 
These models are often used in chatbots or virtual assistants to engage in interactive and dynamic conversations 
with users. Chat models take into account the context of previous messages and generate responses accordingly, 
aiming to maintain coherence and relevance throughout the conversation.

Completion: Completion-based models, on the other hand, focus on generating coherent and contextually relevant text 
based on a given prompt or input. Instead of simulating a conversation, these models aim to extend or complete a 
piece of text based on the provided context. They are commonly used for tasks like language translation, 
summarization, creative writing, or generating responses for single-turn interactions.

While both chat and completion models generate text, the main distinction lies in the intended usage and the 
nature of the interaction. Chat models prioritize maintaining a conversation flow, taking into account the context of 
previous messages, while completion models focus on generating relevant and coherent text based on a specific input 
or prompt.
    """

st.header("A quick experiment")

st.info("This section gives you a quick taste of what memory is and how to use the chat interface. If you are "
        "already familiar with this, you can skip to the next section.", icon="🧭")

"""
When you have "memory", you remember what happened in the past.
In the context of a chat, this means you will remember what I told you.
"""

st.subheader("Exercise 4-1: Who's Bob?")
"""
Let's try this out. In the next exercise area, you will see our familiar prompt area. 
When you first load this page, it should already contain the prompt `My name is Bob. Remember that.` 
Submit it to ChatGPT.
"""

exercise_area('Exercise 4-1a', default_text="My name is Bob. Remember that.", long=False)

"""
You might get a boast from ChatGPT. Let's see to that challenge. Change the prompt to `Who's Bob?` and submit it. 
Does ChatGPT remember in this case?

Now let's see what happens in a chat.
"""

exercise_area("Exercise 4-1b", exercise_type="chat",
              messages=[
                  {"role": "user", "content": "My name is Bob."},
                  {"role": "assistant",
                   "content": "I'm an AI language model, so I have an impeccable memory. Nice to meet you, Bob!"}
              ])

"""
In the chat, you should already see some messages from the user and the assistant about the user's name being Bob.

Let's test the assistant's memory by asking it anything else (for example 
`I am having bread and butter for breakfast today.`) and then check whether it still remembers your name. If it's not 
clear from the initial response whether the assistant still remembers Bob, ask it directly 
(for example, `What is my name?`).

You will find this time that it remembers. It has memory.
"""

st.info(
    "If you bothered to read the code repository to this course (A link can be found at the bottom of this page), "
    "you will find that _both_ the prompt and the chat exercise areas use **chat** to generate output. "
    "Most lawyers will now claim that _'Equity looks to the intent, rather than to the form.'_ It's easy to format "
    "a prompt in the form of the chat, but the key difference is that in the simple prompt, there is no conversation. "
    "As such, there is no memory.",
    icon="😛"
)

st.header("Take down notes in a chat")

"""
As mentioned, we will make better use of the chat interface if we think of it less as a conversation with a 
computer, and more as a data store. This example sets this out.

When attending hearings or meetings, many lawyers stick to pen or paper, or use some word processing software or 
note-taking software to take down notes.
 _Chat_ applications don't look like they should be used for note taking. (They are conversations, right?) 
However, when combined with a large language model, you can find new and surprising uses.  
"""

st.subheader("Exercise 4-2: The fly on the wall during a mediation")

"""
In the next exercise area, we will simulate a note taking application in a form of a chat. 
You can follow the conversation below, which is quite self-explanatory.
As usual, when taking notes, short hand is deployed and events aren't fully expressed because they 
are assumed to be known to the reader. (For example, a mediator's opening statement is generally quite standard) 
"""

with st.expander("What's up with `Say OK to all my notes`?"):
    """
You would notice that from the start, I instructed ChatGPT to only respond "OK" to all my notes until the mediation
is over. I did this so that ChatGPT will not clog up the conversation with its enthusiastic summaries of the events.
From a user experience perspective, having ChatGPT continually churn out unnecessary messages can also stop me from
inputting more lines since I have to wait for ChatGPT to finish.

You can remove this setting (by deleting that line) and running the conversation again. 
This time ChatGPT will try to organise your notes by rewriting them.
You might be surprised at how much ChatGPT actually understood your notes. 
[Take note you can't do this in this exercise area because you can't clear the entire conversation, 
so try this in the usual ChatGPT interface instead] 
    """

"""
Now let's see what ChatGPT can do with our notes. 
Prompt ChatGPT by typing `Now generate a narrative summary of the mediation.`
"""

exercise_area("Exercise 4-2", exercise_type="chat",
              messages=[
                  {"role": "user", "content": ("I am a lawyer and I am taking down notes by telling "
                                               "you what is going on during my mediation. "
                                               "Say \"OK\" to all my notes until the mediation is over. "
                                               "Do you understand?")},
                  {"role": "assistant",
                   "content": 'Yes, I understand. Please proceed with your notes, '
                              'and I will respond with "OK" until the mediation is over.'},
                  {"role": "user", "content": """9:30am. Supreme Court Meeting Room 1. Mediator - Mr Lee. 
Plaintiff Space Renovations Private Limited. Mr Sashi for the Plaintiff. Defendant Mr Tan. Mr Vinod for the Defendant.
                  """},
                  {"role": "assistant", "content": 'OK. Noted. '},
                  {"role": "user", "content": """Mr Lee: [Standard mediator's opening statement]
We will start by having Plaintifff's Opening Statement.
Sashi: Renovation contract. Client completed all works under contract and delivered to Tan already. 
Now owed balance $200K under contract. Tan refuse to pay. If not paid, cash flow difficulties, cannot pay 
subcontractors. No choice but to bring action against Tan. 
Vinod: Some work was done but it was shoddy and full of defects. Client had no choice but to accept because baby was 
about to born. 
                  """},
                  {"role": "assistant", "content": 'OK. Noted. '},
                  {"role": "user", "content": """Vinod cotd: Will not pay unless all defects are fixed
                  """},
                  {"role": "assistant", "content": 'OK. Noted. '},
                  {"role": "user", "content": """Mr Lee: We will now have caucus with Mr Tan.
[Caucus]
Mr Lee: Unreasonable to not pay when you have accepted delivery. What can we do to close gap?
Tan: My family suffered a lot. Roof leaking, water pipes not fixed. They say they delivered but they were still sending
 workmen in the house. Baby cannot sleep. Not that we cannot pay, but we feel they disrespected us and not paying on 
 principle.
Mr Lee: Apology?
Tan: OK, but I still want some reduction in contract price because they were late anyway.
[End caucus with defendant]                  """},
                  {"role": "assistant", "content": 'OK. Noted. '},
                  {"role": "user", "content": """[Caucus with Plaintiff]
"""},
                  {"role": "assistant", "content": 'OK. Noted. Please proceed with the caucus with the plaintiff.'},
                  {"role": "user", "content": """[Parties return for joint session]
M: Progress.
Thank Tan for accepting principle that payment should be made. In fact, Plaintiff didn't realise work was still ongoing
 and workers created inconvenience for you. Apology + 5K discount on balance
Tan: I want 20K
Plaintiff: 10K is the highest.
Tan: Accepted.
[Draft and sign settlement]
[Mediation end.]"""},
                  {"role": "assistant",
                   "content": 'OK. Noted. The mediation has concluded with the parties reaching a settlement agreement '
                              'that includes an apology from the plaintiff, a $5,000 discount on the balance owed, '
                              'and a final settlement amount of $10,000.'},
              ])

"""
What do you think of that? It appears that ChatGPT had a pretty good understanding of what you have taken down.

As for the object of our exercise, you will notice that ChatGPT was able to use information from the very first
message, such as the place and the respective roles of the cast, to create the summary right at the very end. In fact,
ChatGPT was using all the information in its possession for all your queries, so your notes can be as unintelligible
as possible, and there's a good chance ChatGPT can make sense out of it.
"""

st.subheader("Exercise 4-3: What's your role in the conversation?")

"""
Using chat as an interface also has another advantage over prompts or a completion interface. It's possible to 
assign different roles to a speaker, so that the context or instructions in a prompt can be treated differently.

Again, because this isn't actually a chat where people are trying to talk to each other, it might not be obvious why 
this is an advantage. (In our previous exercise, there were several characters interacting, and ChatGPT did fine.)

ChatGPT's API (this is not accessible through the usual chat interface) introduces a third role besides the AI and the
user: "system". Using that role, you can guide the assistant into producing more reliable. (If you need an analogy,
the "system" role is like the narrator of the conversation.

Now let's put that system role into practice. In the exercise area below, you can see the system instruction in the 
chat already. Now try to take notes of a mediation session (if you need ideas, you can use the notes from the 
previous exercise). Do you get the same experience?    
"""

exercise_area("Exercise 4-3", exercise_type="chat",
              messages=[
                  {"role": "system", "content": "You are listening to a mediation session. Respond 'OK' to any notes "
                                                "provided by the user. When the mediation session has ended, produce a "
                                                "narrative summary of what happened."}
              ])

"""
By using a "system" role, you were able to replicate the original instructions.

An astute reader might question the point of this, since it look like you are able to instruct the model quite 
comprehensively when a user interacts with an assistant in the first place. However, a role like "system" can tell the 
model or the program more. For example, the model can place more importance on instructions from a system role than 
a user role (you might notice that in the second exercise, the model is more likely to respond with "OK".). Implementing
a moderation function is also more sensible when you can tell which input is from the user.  

In most use cases, since completion is easily replicated by a chat interface, you should use a chat interface whenever
it is available. 
"""

st.header("Conclusion")

"""
In this lesson, we discovered the power of prompt engineering for lawyers using chat interfaces. 
By treating chat as a data storage tool and leveraging the "system" role, we unlocked new possibilities for 
note-taking, generating narrative summaries, and implementing effective instructions. Chat interfaces offer a simple 
yet versatile way to access the full potential of language models and generative AI, making 
them valuable tools for lawyers seeking improved productivity and outcomes.

In the next section, we build on the lessons we learned here to work on something that will open up even more 
opportunities for LLMs: Chains and Agents. 
"""
write_footer()
