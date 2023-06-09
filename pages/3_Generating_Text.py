import streamlit as st

from helpers import use_custom_css, check_openai_key, write_footer
from prompt_widget import exercise_area, OpenAIModel

st.set_page_config(
    page_title="Generating text using prompts — Prompt Engineering for Lawyers",
    layout="wide"
)

use_custom_css()

check_openai_key()

st.title("Generating text using prompts")

"""
LLMs are exciting because they are able to generate coherent and contextually relevant output. 
They do so by leveraging their training on vast amounts of data to recognise patterns or make predictions.
Compare this with previous approaches which focus on classification, regression or other specific tasks.

In this section, we will showcase how manipulating the input prompts can influence the output generated
by the model.
"""

st.header("Make an Argument for me")

"""
It's possible for an LLM to generate all sorts of content, but for a course for lawyers, let's make ChatGPT
argue a case for us. 
"""

st.subheader("Exercise 3-1: A renter fails to pay the rent")

"""
Here's a scenario that might involve a self-represented litigant. 
Assume you rent a place and have fallen behind on payments. Your landlord has brought an action to recover the rent
and foreclose your lease. 

Let's see how ChatGPT will defend you.  
"""

exercise_area(
    "Exercise 3-1",
    default_text="Title: John vs. Doe \n"
                 "Facts: John leased an apartment from Doe. Under the lease agreement, rent is due in arrears on the 5th day of "
                 "the relevant month. Doe has brought an action to recover the rent and foreclose John's lease. "
                 "John is a food delivery driver and due to a recent accident, has not been able to earn "
                 "enough money to pay the rent in time. If the lease is foreclosed, John's family of four will have no place to "
                 "live. Usually, Doe is understanding and will give John at least a few weeks to pay the rent. However, recently "
                 "there have been many people who are enquiring about renting John's place. Doe's wife has also been giving John "
                 "and his family evil stares recently. \n"
                 "You are John's lawyer. Generate an opening statement."
)

"""
If you thought that ChatGPT's response is amusing, imagine that someone out there might rely on it when representing
himself or herself in court.

Here's a good question: is the opening statement generated by ChatGPT _appropriate_? Maybe, if it's a movie set. 
But litigation is far more complicated than that. For example, a discussion on the equities of the case is wholly
inappropriate during a pre-trial conference to fix hearing dates. You can try to fix that by adjusting the instruction
or the context in the prompt. 

Here are other text you can generate using an LLM:
* A list of arguments for John in bullet points
* A list of arguments for Doe in bullet points
* An outline of a written submission for John
* The text of a Powerpoint presentation in support of John's case   

As you study the arguments generated by ChatGPT, you may question whether _force majeure_ 
or the bit about Doe's wife are viable legal arguments to make in court for a fact situation like this.
It's important to note that LLMs are not lawyers. As noted above, LLMs generate text based on applying 
patterns observed in its training data on the prompt given to the LLM. 
That's not how lawyers find or apply the law. At least theoretically. 
"""

with st.expander("If I cannot get the LLM to do what I want through prompt engineering, "
                 "does this mean that ChatGPT does not have the ability to generate opening statements?"):
    """
It may be difficult to get a LLM to generate the output you want through prompt engineering alone, 
but you have other options, such as training and fine tuning.

**Fine tuning**:  Fine-tuning, in the context of language models, refers to the process of customizing a 
pre-trained model to specialize in a specific task or domain, such as generating legal text. 
It involves training the model further on a narrower dataset that is specific to the desired task, 
such as legal documents or case laws. By fine-tuning, lawyers can adapt the model to understand legal language and 
produce outputs that are more tailored to the legal domain.

**Training**: Training, in the context of language models, refers to the initial process of exposing the model to vast 
amounts of text data from diverse sources. During training, the model learns to recognize patterns, grammar, and 
context within the text. It develops an understanding of how words, phrases, and sentences relate to each other, 
enabling it to generate coherent and contextually relevant responses. Through training, language models gain a broad 
knowledge base, which allows them to generate text and provide insights based on the patterns they have learned from 
the training data.

It's worth noting that while training and fine-tuning can significantly improve the model's output, 
they might not always guarantee the exact desired results. LLMs are probabilistic models, and their output is 
influenced by various factors, including the quality and diversity of training data, prompt engineering, and the 
inherent limitations of the model architecture.

Therefore, it's important to experiment with different prompts, iterate on the fine-tuning process, and incorporate 
human oversight and verification to ensure the output aligns with your expectations and requirements.
    """

st.subheader("Exercise 3-2: In It to Win It")

"""
Despite our misgivings on the practicality of the arguments generated by ChatGPT, let's continue to push it. 
"""

exercise_area(
    "Exercise 3-2a",
    default_text="Title: John vs. Doe \n"
    "Facts: John leased an apartment from Doe. Under the lease agreement, rent is due in arrears on the 5th day of "
    "the relevant month. Doe has brought an action to recover the rent and foreclose John's lease. "
    "John is a food delivery driver and due to a recent accident, has not been able to earn "
    "enough money to pay the rent in time. If the lease is foreclosed, John's family of four will have no place to "
    "live. Usually, Doe is understanding and will give John at least a few weeks to pay the rent. However, recently "
    "there have been many people who are enquiring about renting John's place. Doe's wife has also been giving John "
    "and his family evil stares recently. \n"
    "You are John's lawyer. Come up with a strategy to get Doe to restructure John's overdue payments."
)

"""
This time, the output of ChatGPT appears more feasible and might even be practical advice. Perhaps ChatGPT wouldn't
make a good advocate, but it still has other things to offer. 

We're not done yet. 
"""

exercise_area(
    "Exercise 3-2b",
    default_text="Title: John vs. Doe \n"
    "Facts: John leased an apartment from Doe. Under the lease agreement, rent is due in arrears on the 5th day of "
    "the relevant month. Doe has brought an action to recover the rent and foreclose John's lease. "
    "John is a food delivery driver and due to a recent accident, has not been able to earn "
    "enough money to pay the rent in time. If the lease is foreclosed, John's family of four will have no place to "
    "live. Usually, Doe is understanding and will give John at least a few weeks to pay the rent. However, recently "
    "there have been many people who are enquiring about renting John's place. Doe's wife has also been giving John "
    "and his family evil stares recently. \n"
    "You are John's lawyer. Come up with a strategy to get Doe to restructure John's overdue payments.",
    model=OpenAIModel.GPT4
)

with st.expander("The exercise area can't load because I don't have access to GPT-4"):
    """
GPT-4 still requires you to join a waitlist in order to access it.

If you can't wait, I have produced one of the text generated by GPT-4 so that you can continue this exercise.


> Strategy to get Doe to restructure John's overdue payments:
> * Begin by highlighting John's good history as a tenant. Emphasize that John has been a reliable and responsible 
> tenant in the past and the current issue is due to an unforeseen incident, 
> the recent accident, which has limited his ability to work and earn money.
> * Communicate the implications of foreclosure on John's family. Explain that if the lease is foreclosed, John's wife 
> and children will be left without a place to live, causing significant hardship and stress on the family.
> * Offer a proposed repayment plan. Outline a reasonable and realistic plan for catching up on the overdue rent 
> payments, demonstrating John's commitment to making things right. This plan could include partial payments in the 
> short-term, with a return to full monthly payments once John has recuperated and returned to work.
> * Suggest an amendment to the lease agreement to provide for temporary hardship accommodations. This could include 
> an extended grace period for rent payment in the event of unforeseen circumstances, like illness or job loss, 
> or a temporary reduction in rent due to a loss of income.
> * Propose a meeting between John, Doe, and their respective legal counsel to discuss potential solutions amicably. 
> This would provide an opportunity for the parties to come to a mutually beneficial arrangement 
> while maintaining a positive working relationship.
> * Remind Doe of the potential cost and effort involved in finding a new tenant. 
> This includes marketing costs, lost rental income, and the time-consuming process of screening prospective tenants.
> * If all else fails, consider exploring alternative dispute resolution methods, such as mediation or arbitration, 
> to avoid costly litigation and maintain the integrity of the landlord-tenant relationship.
    """

"""
Astute readers might notice that we are now using GPT-4 instead of ChatGPT. We can now compare the output of the models.
What do you think?

We can also test the capabilities of each model by tweaking the instruction and then seeing how differently each 
model reacts to a slightly different prompt. (For example, instead of asking the model to restructure John's payments,
ask it to force Doe to drop the lawsuit or bring the parties to mediation.) 
Remember that if you ask a LLM to regenerate its response to the same prompt, it can come up with a varied reply.

In my view, the output from GPT-4 appears richer (there's a bigger variety of words used) and looks more detailed. 
Generally speaking, for tasks which need more complex reasoning such as coming up with a strategy or actions,
it is worth considering using a more powerful model. The flip side is that powerful models are more expensive and 
might take more resources (including time) than other models.  
"""

st.warning("The second exercise area uses GPT-4, which costs ten times more than ChatGPT. "
           "It would still take a lot of queries to incur a significant cost, "
           "but GPT-4 will get you there much sooner than ChatGPT. Use with caution.", icon="💰")

with st.expander("What's the difference between ChatGPT and GPT-4?"):
    """
ChatGPT and GPT-4 are both large language models, but they have some key differences. 
ChatGPT is a generative pre-trained transformer model, while GPT-4 is a generative pre-trained transformer model 
with a few key improvements. These improvements include:

* A larger model size, with 175 billion parameters compared to ChatGPT's 1.5 billion parameters.
* A more sophisticated training method, which uses a technique called "attention" to help the model learn to focus 
on the most important parts of a sentence.
* A wider range of training data, which includes text from a variety of sources, including books, articles, and code.

These improvements make GPT-4 a more powerful and versatile language model than ChatGPT. It can generate more realistic 
and informative text, and it can be used for a wider range of tasks, such as translation, writing, and coding.
    """

st.header("Doing Legal Research with ChatGPT?")

"""
If you knew _anything_ about Prompt Engineering, you are probably aware that ChatGPT, as well as other large language
models, are known to "hallucinate". 

By "hallucinating", these models produce output which is not based on reality or factually incorrect. However, due
to the way users ask for such information, and the way it is presented, there's a strong likelihood that an 
unsuspecting user would take such output to be the truth.

In the legal domain, a lawyer representing a man who sued an airline relied on ChatGPT to help prepare a court filing. 
[It did not go well](https://www.nytimes.com/2023/05/27/nyregion/avianca-airline-lawsuit-chatgpt.html?unlocked_article_code=3g7DDz3SJ6_uKgb94Z3rvuxJ-9bWZFtpey_e9W9uRBoCcufQ0tzZlXveRrJlbvNzny4z3GK_vJbsAT-DM425i9q1D72a77NoV7OnKL8vUoXz6xvhJkvVt-FN715J0HzSAae4uUZfDoj11UXvXS7WgCer5tqd6_TzfMeG2kBM6zzzSWkHGwEUTuI5QNDSmGV4HFnq2195sBj6AiKRIAQTfHdHLWuuXJP6cwOSSoNT9LVMEbNQn9KvhENnE6neJYtkMlYs9Xy_-5Ytj6D4dMHy5O2LL0O04_S5_Z6TPaMGgvyj2W-o2uQiYpYjIN51-xfhDyX6tMYB8jIOrKLtO3u6TD4t1bL3-jCRAjg&smid=url-share).

If you followed the text in the previous sections, you would know why using large language models to perform legal
research is a bad idea. The large language models generate text based on probabilities observed in its training data.
This is not how lawyers do legal research.

It's possible to ameliorate the effects of hallucination through prompt engineering. For what it's worth, you can tell
ChatGPT to say "No" if it could not find an answer.

There are other prompt engineering techniques which we will cover in upcoming sections which will help reduce the risk
of hallucination. It's still important to recognise that large language models should not be used to generate critical 
content, especially when such content relies heavily on facts and logic. You, or an expert, should check the content
 that is generated. After all, large language models are not lawyers.
"""

st.header("Conclusion")

"""
Hopefully, you were able to get a taste of the generative capabilities of LLMs. By giving specific and concise prompts,
you can get a LLM to generate a wide range of text.

There are issues of whether the text generated is appropriate for the circumstances, which could be fixed by adjusting 
the prompt, training or fine-tuning. It may also be useful to think about indirect uses such as generating an outline 
of the statement or submission, instead of the actual submission itself. 

This exercise also tried to get you to experiment with using different models and comparing their output. 
Do consider the circumstances of your use case to select the right model to use. 

In the next section, we will be dealing with memory, using a chat interface. 
"""

write_footer()
