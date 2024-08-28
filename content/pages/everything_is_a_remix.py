import streamlit as st

# A page template to keep track of all the helper functions and classes that are used in the project.
# Make a copy of this page to begin a new page
from helpers import navigation_footer, check_openai_key, write_what_you_will_learn
from prompt_widget import simple_prompt

# Page path is used to identify the page in the navigation footer. Use the file path to the page.
PAGE_PATH = "content/pages/everything_is_a_remix.py"

# If this page has exercises, use the check_openai_key() function to check if the user has an OpenAI key.
# Remove this if it is an essay.
check_openai_key()

# Title of the page
st.title("Everything is a Remix: Transforming contract clauses with LLMs")

# A widget to summarise what you will learn on this page
write_what_you_will_learn([

])


exercise_2 = "Make sense of a contract clause"
st.header(exercise_2)

"""
As we progress from basics, we are starting to see the power of LLMs apply to legal tasks.

In this exercise, we will use a contract clause and ask the LLM to explain it in plain English.
This can simplify and clarify the language of the clause, making it easier to understand for non-lawyers.

I've borrowed a confidentiality clause. It's not the most complicated contract clause, but it could use some 
improvement. Let's see what the LLM can help us with.
"""

simple_prompt(exercise_2,
              default_text="Rewrite this confidentiality clause to be more simple and plain: \n "
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

"Do you agree that the output is easier to read now?"

# Navigation footer is a common footer that is used in all pages. It provides links to the previous and next pages.
navigation_footer(PAGE_PATH)
