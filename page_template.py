import streamlit as st

# A page template to keep track of all the helper functions and classes that are used in the project.
# Make a copy of this page to begin a new page
from helpers import navigation_footer, check_openai_key

# Page path is used to identify the page in the navigation footer. Use the file path to the page.
PAGE_PATH = "content/pages/page_template.py"

# If you want to write an essay, use the write_essay_page() function.
# It highlights to users of pages that are essays.
# write_essay_page()

# If this page has exercises, use the check_openai_key() function to check if the user has an OpenAI key.
# This allows the user to use OpenAI's GPT-3 API to complete exercises.
# Remove this if it is an essay.
check_openai_key()

# Title of the page
st.title("Page Template")

"""
Continue to enter page content here.
"""

# Navigation footer is a common footer that is used in all pages. It provides links to the previous and next pages.
navigation_footer(PAGE_PATH)

# TODO: Remember to add a link to the page in routes.py to make it accessible in the app.
