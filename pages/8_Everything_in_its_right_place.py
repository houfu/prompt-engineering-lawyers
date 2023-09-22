import streamlit as st

from helpers import use_custom_css, check_openai_key, write_footer
from prompt_widget import exercise_area

st.set_page_config(
    page_title="Everything in its right place — Prompt Engineering for Lawyers",
    layout="wide",
)

use_custom_css()

check_openai_key()

st.title("Everything in its right place")
st.subheader("Introduction")
"""
The easiest way to understand ChatGPT and large language models is that they are constantly trying to predict what
the next word is given the preceding text. This way, we can say that large language models are good at "generating" text.

Another task which is important for computers working with language is "categorising". This task can be defined like
this: given a text, which of the previously defined categories or labels apply to it? A common example of this task
is sentiment analysis -- the model tries to figure out whether a customer's review is bad or good. After categorising
the type of review, you can perform other actions like how to follow up etc. 

It turns out that with prompting, large language models can produce good results at categorising. In this exercise,
we will explore some uses and limitations. 
"""

st.subheader("Exercise 8-1: Legal or Not Legal?")
"""
Let's dive straight into this.  Imagine you are the sole lawyer in a company of 5,000 employees. You also happen
to be well loved by all your colleagues who admire your helpfulness and all-round smartness. They _love_ asking you 
questions. 

Unfortunately, because you would like to go home at some point of the day, you need to sieve questions which actually
relate to your job to answer. In this sense, you are grouping or categorising questions into 2 categories: legal or 
not legal. 

In the exercise area below, I have provided a quick prompt which will allow you to do this. Try various types of 
questions and test whether ChatGPT got it right or wrong. You might be surprised that ChatGPT does pretty all right
most of the time. 
"""

exercise_area(
    "Exercise 8-1",
    long=True,
    default_text="You are an in-house lawyer and your task is to determine whether the following question is related to your work. "
    'Only answer as either "Legal" or "Not Legal".\n\n '
    "The question: If I breach a contract, do I have to pay damages?",
)

"""
The previous exercise can be referred to as **zero-shot**. This means we asked ChatGPT to use its understanding of 
the context and general knowledge learned during its training to make an accurate prediction or meaningful response.
On the one hand, this shows how powerful ChatGPT, and on the other hand, it's convenient for a user because the user
does not need to provide much prompting or guidance to the model. 

But consider this question: "If it's raining, can I sue the sky?" At first glance, the question is a 
legal one because of the word "sue". However, as a company lawyer, this surely has nothing to do with your job. 
Try it: ChatGPT will probably answer this as "Legal".

While this is a clear cut example, I wouldn't suggest that ChatGPT has failed. (You might be specialising in space law
after all) Its answers are based on its general understanding after all. In order to fix this, you need to give it more
guidance. 
"""

st.subheader("Exercise 8-2: Give it a few more shots")
"""
In the previous exercised, you were introduced to the term "Zero-shot" and its limits. In order to improve the model's
answers you have to give it more guidance. We are going to change this from "Zero-shot" to "Few shot". This typically
involves providing the model with a small number of examples or context to perform a specific task or answer a question.
"""

exercise_area(
    "Exercise 8-2",
    long=True,
    default_text="You are an in-house lawyer and your task is to determine whether the following question is related to your work. "
    'Only answer as either "Legal" or "Not Legal".\n\n'
    'Question: "If the product catalogue contains misrepresentations, are we liable?" Answer: Legal \n'
    'Question: "Our customer claims our products are under warranty, can you check the contract?" Answer: Legal \n'
    'Question: "If someone calls me a liar, can I sue them?" Answer: Not Legal \n'
    'Question: "My ex-wife refused to give me access to my children, what can I do?" Answer: Not Legal \n'
    "Question: \"I've got a speeding ticket. What happens if I don't pay the fine?\" Answer: Not Legal \n\n"
    "The question: If I breach a contract, do I have to pay damages?",
)

"""
Try a few more queries and check the answers ChatGPT provides. You may find that the answers are more attuned to the 
nuances displayed in your examples. These examples help guide the model's understanding of the task and 
provide specific context for generating a response.

Let's check whether the kind of examples you provide affects the answer. 

1. Cut the speeding ticket example. (You are going to paste it back to the prompt soon)
2. Ask ChatGPT an issue about traffic offences. 
(For example, "I received a ticket for busting a red light. What happens?") 
Does ChatGPT answer it as "Legal"?
3. Paste the speeding ticket example back and ask ChatGPT again. Did ChatGPT answer differently 
depending on the example given?
4. You can also experiment by switching around the "Legal" or "Not Legal"
answers in the examples and see if there is any impact. 
5. You can also invent a rule (for example, it is Legal when company property is involved) 
and writing a few examples around that rule. Could ChatGPT figure it out on its own?

This shows you that the examples you pick as part of your prompt has a big impact on the performance of your model.

"""
with st.expander("Measuring accuracy using Precision, Recall and F1-Score"):
    """
    Let's learn more ways to discuss the accuracy of a model. Three measures are generally used:
    Precision, Recall and F1-Score.

    **Precision**:

    * Precision is like a measure of how careful the model is when it says a question is a legal matter.
    It's the percentage of questions it correctly identifies as legal out of all the questions it says are legal.
    * So, if your program says 80 questions are legal, and 70 of them are actually about legal matters,
    then the precision is 70/80, which is 87.5%. This means it's pretty good at not falsely claiming
    non-legal questions as legal.


    **Recall**:

    * Recall is like a measure of how thorough your model is in finding all the legal questions.
    It's the percentage of all the actual legal questions that your program correctly identifies.
    * For example, if there are 100 legal questions in total, and your model correctly identifies 70 of them,
    then the recall is 70/100, which is 70%. This means it's capturing a good portion of the actual legal questions.

    **F1-Score**:

    * The F1-score is like a balance between precision and recall.
    It gives you a single number that represents both how careful and how thorough your program is.
    It's calculated using this formula: F1-Score = 2 * (Precision * Recall) / (Precision + Recall).
    * So, if your program has a precision of 87.5% and a recall of 70%,
    the F1-score will be a single number that reflects both these values.

    By using these measures, you are better able to measure the risks of using the model. For example, does it get
    the answer right more often or not? Does it collect all or most of the cases which needs to be identified?
    """

"""
Other than designing better examples or prompts, the other way to improve the accuracy of your model is to fine tune
your model or train one. (We discussed what fine tuning and training is in "Generating Text") Fine tuning or training
is however not always available due to the costs and the resources involved. 

As such, you should always have "few shot" prompts as part of your prompt engineering armoury.  
"""

st.subheader("Exercise 8-3: From binary to multi-class")
"""
Large language models aren't only capable of binary classification (for example, the true/false, or the legal/not legal 
problem previously). They can also categories into one of three or more possible classes or categories.

Let's push ChatGPT's capabilities to classify. We're still in our legal department but now we have three staff,
each with their own basic capabilities as described in the prompt. Let's see if ChatGPT can assign the right
lawyers to a question.  
"""

exercise_area(
    "Exercise 8-3",
    long=True,
    default_text=
    "This is a legal department and your task is to assign lawyers Tom, Dick and/or Harry to work on a legal question. "
    'Only answer by either selecting any of "Tom", "Dick" or "Harry" .\n\n'
    'The description of each lawyer\'s role is as follows: Tom is good at resolving disputes, Dick is good at drafting '
    'agreements and contracts, while Harry is a senior lawyer with strong relationships internal and external. \n\n'
    'Question: "If the product catalogue contains misrepresentations, are we liable?" Answer: Tom \n'
    'Question: "We need to find an expert in forensic science and accounting for this dispute." Answer: Tom, Harry \n'
    'Question: We need to enter into a joint venture agreement with another titan of our industry. What '
    'are the documents we need? Answer: Dick, Harry \n'
    'Question: We need to draft a settlement agreement with our contractor for breach of contract. Answer: Tom, Dick \n'
    "Question: Could you help me write a termination agreement for this contract? Answer: Dick \n\n"
    "The question: If I breach a contract, do I have to pay damages? \n"
    "Answer: ",
)

"""
Make sure you try different questions and see if you agree with the answers the model gives you.

It's possible that the answers to which lawyer should be assigned to an issue is not so objective.
For example, even if Harry is great as the most senior lawyer in the department, he may be dealing with other
responsibilities other than advising colleagues directly. On the other hand, it may be important for the purposes
of training or business continuity that a lawyer is involved even if it is not his specialty. ChatGPT does not
consider these points currently.

Even if we disagree with the answers that the model provides, or the model provides answers which are flat out wrong,
it is still important to consider the consequences. Our (human) lawyers are not automatons. If they receive a question
which they are not suited for or they believe more or less lawyers are involved, they can adjust the situation 
accordingly. This way, the consequences of the model being inaccurate is actually pretty mild.
The value of a system that diagnoses a question accurately _most of the time_ will save value time
for the legal department. 

Accepting that models do not need to achieve 100% accuracy has more implications than you might expect. 
You do not need to invest in extensive data labelling or training or fine tuning of models. With prompt engineering,
ChatGPT can already perform the task sufficiently for you. For the user, the experience is improved since 
the model has lower requirements to run and respond. 

Nevertheless, we can help increase the trust of our model by asking it to explain its classification. See if you can
modify the prompt in the exercise area to explain its answer. (**Hint**: The easiest way is think step by step in the 
answer field)
"""


st.header("Conclusion")

"""
In this lesson, we discovered an effective way to combine prompt engineering with large language models to provide a 
classifier. Previously, classification models required large training data to achieve some accuracy, but you now have
access to such tools through zero shot or few shot. Such valuable options should always form part of the toolkit of a
user.

It's important to note that models rarely achieve 100% accuracy, and counter-intuitively for many lawyers, 
a model which gets the answer right half the time may still be useful in certain contexts. In many real-world 
applications, there are trade-offs between different metrics like accuracy, precision, recall, and cost. 
A strategy that doesn't insist on high 
accuracy allows for a more balanced consideration of these trade-offs to meet specific business or operational needs.
"""
write_footer()
