import streamlit as st

from helpers import use_custom_css, check_openai_key, write_footer
from prompt_widget import exercise_area

st.set_page_config(
    page_title="Can ChatGPT think like a lawyer? — Prompt Engineering for Lawyers",
    layout="wide"
)

use_custom_css()

check_openai_key()

st.title("Can ChatGPT think like a lawyer?")

st.info(
    "This section is inspired by [Yu, Fangyi, Lee Quartey, and Frank Schilder. "
    "'Legal Prompting: Teaching a Language Model to Think Like a Lawyer.' arXiv preprint arXiv:2212.01326 "
    "(2022)](https://arxiv.org/abs/2212.01326). It's useful to read scientific papers!",
    icon="📃"
)

"""
In a previous section, I declared that ChatGPT is not a lawyer:

>It's important to note that LLMs are not lawyers. As noted above, LLMs generate text based on applying 
> patterns observed in its training data on the prompt given to the LLM. 
> That's not how lawyers find or apply the law. At least theoretically. 

Let's challenge this assumption.

One of the tasks a lawyer is trained to do is to examine the facts, identify the relevant legal principles, 
and consider potential implications.

We will do this by providing the model with a fact pattern, then present it some legal principles, and ask  
for its opinion on whether the provisions applies to a fact pattern.
"""

st.subheader("Exercise 7-1: A control experiment")

"""
Before we use any fancy prompt engineering techniques, let's ask ChatGPT directly for the answer (aka "zero shot"). 
We might have detailed prompts about how to perform our tasks, but it's useful to always check our model directly
to see how far we have to go and check how much we have improved our output. 

In the exercise area, I have provided a prompt for the answer we would be exploring in this exercise.
"""

with st.expander("What is a Housing Development Board (HDB) Flat?"):
    """
Our international readers may not be familiar with the subject of this problem. Here's a brief introduction.

A Housing Development Board (HDB) flat refers to public housing in Singapore that is developed and managed by the 
Housing and Development Board (HDB), a government statutory board. HDB flats are subsidized, affordable residential 
units intended for Singaporean citizens and permanent residents.
HDB flats are typically high-rise apartment buildings, although there are also some low-rise and walk-up flat designs. 
These flats are sold on a leasehold basis, with lease durations typically ranging from 99 years to 999 years.

HDB flats have played a significant role in Singapore's housing policy, providing affordable and quality housing 
options for its residents. The HDB aims to create sustainable and cohesive communities, fostering social integration 
and promoting homeownership among Singaporeans.

Read more in [Wikipedia](https://en.wikipedia.org/wiki/Public_housing_in_Singapore).
    """

exercise_area("Exercise 7-1",
              default_text="Fact: In Singapore, Mr. Tan, a retiree, decided to sell his "
                           "Housing Development Board (HDB) flat "
                           "after living in it for several decades. He listed the flat for sale at the market price "
                           "and soon received an offer from Ms. Lee, a young working professional looking for a new "
                           "home.\n Ms. Lee was excited about the flat's location and the amenities it offered. "
                           "She quickly arranged a meeting with Mr. Tan to negotiate the terms of the sale. "
                           "During the meeting, Mr. Tan mentioned that the flat was in excellent condition and did "
                           "not require any major repairs. Trusting Mr. Tan's words, Ms. Lee agreed to purchase the "
                           "flat without conducting a thorough inspection. \n After the sale was finalized and Ms. Lee "
                           "moved into the flat, she discovered several issues that were not disclosed by Mr. Tan. "
                           "The flat had significant water leakage problems in the bathroom, and the electrical wiring "
                           "was faulty, causing frequent power outages. "
                           "The cost of repairing these issues was substantial, "
                           "and Ms. Lee felt deceived by Mr. Tan's failure to disclose them. \n\n"
                           "Question: Can Ms Lee cancel the sale?")


"""
Read the response you will generate. It might mention something about misrepresentation and suggest that the sale can
be cancelled. It might also tell you to consult a lawyer. It's not a terrible response, but it's not how a lawyer
would respond.
"""

st.subheader("Exercise 7-2: Give ChatGPT a legal basis")
"""
We can laugh about this later, but it isn't useful or "lawyerly" to claim that the answer to a legal question is that
"it depends".

To be fair to ChatGPT,  there's no reason why ChatGPT should give a legal answer when it has no basis to do so.
Let's nudge ChatGPT a bit by providing some legal principles. For this, I have copied a [freely available description
on the law of misrepresentation in Singapore](https://www.singaporelawwatch.sg/About-Singapore-Law/Commercial-Law), 
paragraph 8.10.4 and called it a "Legal Rule". 
It's of general application, so you can imagine that it came from a law textbook. 

Let's see what ChatGPT does with that.
"""

exercise_area("Exercise 7-2",
              default_text="Fact: In Singapore, Mr. Tan, a retiree, decided to sell his "
                           "Housing Development Board (HDB) flat "
                           "after living in it for several decades. He listed the flat for sale at the market price "
                           "and soon received an offer from Ms. Lee, a young working professional looking for a new "
                           "home.\n Ms. Lee was excited about the flat's location and the amenities it offered. "
                           "She quickly arranged a meeting with Mr. Tan to negotiate the terms of the sale. "
                           "During the meeting, Mr. Tan mentioned that the flat was in excellent condition and did "
                           "not require any major repairs. Trusting Mr. Tan's words, Ms. Lee agreed to purchase the "
                           "flat without conducting a thorough inspection. \n After the sale was finalized and Ms. Lee "
                           "moved into the flat, she discovered several issues that were not disclosed by Mr. Tan. "
                           "The flat had significant water leakage problems in the bathroom, and the electrical wiring "
                           "was faulty, causing frequent power outages. "
                           "The cost of repairing these issues was substantial, "
                           "and Ms. Lee felt deceived by Mr. Tan's failure to disclose them. \n\n"
                           "Legal rule: Misrepresentation is a ground for relief only where it has induced a contract. "
                           "Clearly, if a person is unaware of the representation, or knows that it is untrue, or does "
                           "not believe it to be true, he or she cannot reasonably have relied on, or be induced by, "
                           "the representation to enter into the contract. \n\n"
                           "Question: Can Ms Lee cancel the sale?")

"""
You would find that ChatGPT produces a very similar reply. If you look closely though, you might find traces of the 
legal rule we provided in its answer. (It's questionable whether this was done because of the prompt or it was from the
training data.)

We have to do better.
"""

st.subheader("Exercise 7-3: The magic words: _Let's think step by step_")
"""
I don't like to think of prompting as 'magic words'. As we've shown throughout this course, prompting a model is not
achieved by saying a few magic words, like "abracadabra" :magic_wand:.
However, if there are truly magic words in this field, "let's think step by step" is probably one of them.

By using "let's think step by step" in your prompt, ChatGPT will lay out its "reasoning" in its response. 
I have added the line at the end of the prompt. Let's see what happens. 
"""
exercise_area("Exercise 7-3",
              default_text="Fact: In Singapore, Mr. Tan, a retiree, decided to sell his "
                           "Housing Development Board (HDB) flat "
                           "after living in it for several decades. He listed the flat for sale at the market price "
                           "and soon received an offer from Ms. Lee, a young working professional looking for a new "
                           "home.\n Ms. Lee was excited about the flat's location and the amenities it offered. "
                           "She quickly arranged a meeting with Mr. Tan to negotiate the terms of the sale. "
                           "During the meeting, Mr. Tan mentioned that the flat was in excellent condition and did "
                           "not require any major repairs. Trusting Mr. Tan's words, Ms. Lee agreed to purchase the "
                           "flat without conducting a thorough inspection. \n After the sale was finalized and Ms. Lee "
                           "moved into the flat, she discovered several issues that were not disclosed by Mr. Tan. "
                           "The flat had significant water leakage problems in the bathroom, and the electrical wiring "
                           "was faulty, causing frequent power outages. "
                           "The cost of repairing these issues was substantial, "
                           "and Ms. Lee felt deceived by Mr. Tan's failure to disclose them. \n\n"
                           "Legal rule: Misrepresentation is a ground for relief only where it has induced a contract. "
                           "Clearly, if a person is unaware of the representation, or knows that it is untrue, or does "
                           "not believe it to be true, he or she cannot reasonably have relied on, or be induced by, "
                           "the representation to enter into the contract. \n\n"
                           "Question: Can Ms Lee cancel the sale? Let's think step by step.")
"""
Isn't that a marked improvement? You can see that ChatGPT is now applying the rule to the facts. 
You might be fooled that it has become a real lawyer.

It's an interesting question why simply adding "Let's think step by step" can produce such a result. (Could it be 
the way the training data was formatted?) In any case, this is a useful quick fix if you need to generate an answer
that requires some advanced reasoning. 
"""

st.subheader("Exercise 7-4: Now once more, with _legal_ reasoning")
"""
We've got ChatGPT to be more logical, but we still need to push ChatGPT harder to think like a lawyer. 

To do this, we will have to go back to basics. We are now travelling to a distant past when we are first year law
students, and we are attending legal analysis and research classes.

We need ChatGPT to perform the steps our first year law students have to do:

1. Describe the issue
2. Identify the applicable legal rule
3. Apply the legal norm to the issue
4. Conclude

I've modified the prompt to nudge ChatGPT to do this exercise. Let's see what ChatGPT can do. 
"""
exercise_area("Exercise 7-4",
              default_text="Fact: In Singapore, Mr. Tan, a retiree, decided to sell his "
                           "Housing Development Board (HDB) flat "
                           "after living in it for several decades. He listed the flat for sale at the market price "
                           "and soon received an offer from Ms. Lee, a young working professional looking for a new "
                           "home.\n Ms. Lee was excited about the flat's location and the amenities it offered. "
                           "She quickly arranged a meeting with Mr. Tan to negotiate the terms of the sale. "
                           "During the meeting, Mr. Tan mentioned that the flat was in excellent condition and did "
                           "not require any major repairs. Trusting Mr. Tan's words, Ms. Lee agreed to purchase the "
                           "flat without conducting a thorough inspection. \n After the sale was finalized and Ms. Lee "
                           "moved into the flat, she discovered several issues that were not disclosed by Mr. Tan. "
                           "The flat had significant water leakage problems in the bathroom, and the electrical wiring "
                           "was faulty, causing frequent power outages. "
                           "The cost of repairing these issues was substantial, "
                           "and Ms. Lee felt deceived by Mr. Tan's failure to disclose them. \n\n"
                           "Legal rule: Misrepresentation is a ground for relief only where it has induced a contract. "
                           "Clearly, if a person is unaware of the representation, or knows that it is untrue, or does "
                           "not believe it to be true, he or she cannot reasonably have relied on, or be induced by, "
                           "the representation to enter into the contract. \n\n"
                           "Question: Can Ms Lee cancel the sale? Please analyse this question according to the "
                           "following legal reasoning approach: Issue, Rule, Application, Conclusion.")
"""
What do you think of that? Did ChatGPT:

1. Identify the right issue to resolve?
2. Identify the correct rule to apply?
3. Apply the rule to the facts of the case?
4. Make a conclusion which follows from the previous statements? 

It's no secret that large language models are able to 
[pass the bar exam](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4389233). 
"""

st.header("Conclusion")
"""
In this section, we were able to demonstrate that with the right prompts, we can get ChatGPT and large language models
to reason like a lawyer. The most immediate uses for this is legal research: ChatGPT can elaborate on the links between
the application of legal rules to facts.

As a demonstration, this exercise has obvious limitations. We gave ChatGPT the answer by selecting the legal rule it 
would apply. Eagle eyed observers would also note, for one, that ChatGPT did not pick up on what "cancel" the contract 
means. The rule we gave ChatGPT, which ChatGPT relied heavily on, is at once too wide and too narrow at the same time.
The law of misrepresentation is not easy to condense into a pithy paragraph. 
"""

write_footer()
