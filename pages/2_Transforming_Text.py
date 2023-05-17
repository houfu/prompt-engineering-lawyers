import streamlit as st

from helpers import use_custom_css, check_openai_key, write_footer
from prompt_widget import exercise_area

st.set_page_config(
    page_title="Text transformation using prompts — Prompt Engineering for Lawyers",
    page_icon=":home:",
    layout="wide"
)

use_custom_css()

check_openai_key()

st.title("Text transformation using prompts")

"""
One of the easiest and effective ways to use a large language model is to transform a text you have using prompts.

By providing the model with a starting point, such as a sentence or a paragraph, we can use prompts to 
guide the language model towards generating new and original content that is closely related to the original input. 
This can be done for a wide range of tasks, such as summarization, paraphrasing, translation, and more.
"""

st.header("Rewrite an email to get the tone you want")

"""
Lawyers email clients a lot. Clients want updates faster and faster, but lawyers suffer from being human.
They might be too tired to write an email that sounds professional.
Here a LLM can "correct" the tone of the email to be more professional.
"""

st.subheader("Exercise 2-1: It's Been a Hard Day.")

"""
Let's ask ChatGPT to check our draft email, and make it sound professional.
"""

exercise_area("Exercise 2-1",
              "I am a lawyer writing an email to my client. This is my email: "
              "Hey I just wanted to tell you that I went to court today and man the wait was so long. "
              "When I finally got to speak to the Judge, he was like are you all ready for trial? "
              "I told him you still had to make a few more discovery application, "
              "and my learned friend from the other side was like seriously they had a window to do this. "
              "I vigorously argued for an extension of time. It was granted but you have to pay costs. "
              "So now, you have to file your application in two weeks. Next appointment with the judge, in four weeks. "
              "Let me know if you have any questions!  \n\n Rewrite my email in a more professional manner.")

"""
You might be surprised that ChatGPT was able to fix grammar errors, get rid of colloquialisms and produce a fairly
decent email. It even knew what your email was.

It's useful to think about this prompt in two parts:
 
1. the context  
2. the instruction.
 
The context provides the LLM with a background of what it needs to know, while the instruction tells the LLM what
it needs to do. As you can see from the previous prompt, they are separated into two paragraphs. 
Once you understand this paradigm, you can write lots of effective prompts. 

Here's a follow up exercise. See if you can figure out where the instruction is. If you can, a whole new adventure
awaits you! Ask the LLM to do the following instead of writing in a professional tone.

* Write the email in a form of a haiku
* Write the email in the voice of a pirate lawyer
* Write the email in Singlish (or whatever local dialect you can think of).
"""

st.info(
    "While the idea of allowing an AI to edit your work may seem unsettling, it's worth noting that this concept "
    "is not entirely new. A prime example of this is Github Copilot, a renowned AI tool leveraging LLMs, "
    "which aims to enhance code quality for software developers. "
    "Its main purpose is to facilitate a collaborative coding approach known as 'pair programming,' "
    "where one programmer writes the code while the other reviews it and provides suggestions. "
    "By drawing a parallel, we can envision how a lawyer equipped with a suitable LLM could utilize a similar "
    "technique to enhance the quality and accuracy of their work. ",
    icon="☝️"
)

st.header("Rewriting contract clauses")

"""
Let's take the context-instruction paradigm further.

Contract clauses are specific provisions or terms included in a legal agreement that help define the 
rights and responsibilities of the parties involved. "Traditional" contract language is inaccessible to most
people.

LLMs can be a valuable tool in simplifying and clarifying contract clauses to make them more accessible 
and easier to understand. By utilizing its language generation capabilities, LLMs can assist in transforming complex 
legal language into plain and straightforward terms. This process involves breaking down convoluted sentences, 
replacing jargon with simpler alternatives, and reorganizing the structure of the clause to enhance readability.  
"""

st.subheader("Exercise 2-2: Making sense out of a clause.")

"""
I borrowed this confidentiality clause from [Law Insider](https://www.lawinsider.com). It does not qualify as
the most complicated contract clause I have ever seen, but it could use some improvement. Let's see what ChatGPT can do 
with it. 
"""

exercise_area("Exercise 2-2",
              "Rewrite this confidentiality clause to be more simple and plain: \n "
              "The Tenant hereby declare and warrant that the Tenant shall at any time be obliged to keep confidential "
              "all the information obtained including but not limited to the terms of this Tenancy Agreement, "
              "other agreements, statements, the contents of any discussions or negotiations between the parties prior"
              " to the signing of this Tenancy Agreement or the Landlord’s trade secret acquired due to the leasing "
              "of the Premises, and shall take such actions including but not limited to taking effective measures to "
              "prevent the aforesaid contents or trade secrets from being disclosed to any third party (other than "
              "the disclosure to the Tenant’s legal adviser or employees or agents in connection with the signing and "
              "execution of this Tenancy Agreement; and other than disclosure by the Landlord in compliance with the "
              "judicial or administrative orders legally made by state organs, governmental institutions, courts or "
              "social organizations) and refraining from using the aforesaid contents or trade secrets in any form, "
              "failing which the Tenant shall be deemed to be in breach of Clause 7.1 hereof, the Landlord shall be "
              "entitled to exercise all the Remedial Rights according to such clause.")

"""
If you're a common law contracts lawyer, read the output and think about whether you would recommend this language 
in your contracts. 

The answer is a big, fat NO. The clause you generated probably leaves out references such as "Remedial Rights" and 
the location of the clause dealing with breaches of this agreement. Let's ask ChatGPT whether it would replace the
clause with its language:

> As an AI language model, I am not a lawyer and cannot provide legal advice or directly amend contracts. 
> My previous response was a simplified and plain-language interpretation of the confidentiality clause you provided. 
> If you require legal assistance or contract amendments, it is recommended to consult with a qualified attorney 
> who can review your specific situation and provide professional guidance. 
> They will be able to draft or modify the confidentiality clause in accordance with applicable laws and 
> the specific requirements of your agreement.

Although you might argue that ChatGPT tried to duck this one, there are some truths in its statement:

* ChatGPT (as well as any general purpose LLMs) are trained on big piles of texts, not contracts. It is thus expected
to generate text conforming to its training data.
* It's unfair to expect ChatGPT, or a lawyer, to understand the specific situation from one clause.
* Unauthorised practice of law is a real issue. 

That being said, let's see whether modifying the instruction (say, "rewrite for lawyers") can yield better results.
I will let you be the judge of whether a clearer prompt improved ChatGPT's answer.

"""

st.header("Conclusion")

"""
In conclusion, the use of LLMs in law offers opportunities to transform and simplify text through effective prompts. 
While LLMs can improve language, they have limitations due to their general training and the need for human expertise. 
Rewriting contract clauses with LLMs can enhance accessibility, but legal advice remains essential. 
Harnessing LLMs requires a discerning approach, balancing their potential with human knowledge and
 ethical considerations. LLMs are powerful tools to enhance efficiency and accessibility in the legal field. 

In the next part, we will explore how to exploit the generative capabilities of LLMs. 
"""

write_footer()
