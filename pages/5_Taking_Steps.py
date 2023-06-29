import streamlit as st

from helpers import use_custom_css, check_openai_key, write_footer
from prompt_widget import exercise_area

st.set_page_config(
    page_title="Taking Steps — Prompt Engineering for Lawyers",
    layout="wide"
)

use_custom_css()

check_openai_key()

st.title("Taking Steps")
"""
By now, you would have learned that the prompts we can provide to a large language model can take a variety of forms and
produce all sorts of output. The inherent flexibility of a large language model is one of its greatest strengths,
which make it very useful for a wide variety of uses.

In this section, we will use ChatGPT in a step by step approach to generate an agreement. We will use the output 
generated in the previous step to work on the next step. Such an approach is very useful when we need to refine 
our inputs and outputs.  
"""

st.subheader("Exercise 5-1: (Just) Draft a Non-Disclosure Agreement")
"""
Let's get ChatGPT to create a non-disclosure agreement. I chose a non-disclosure agreement as it is a relatively
straightforward agreement to demonstrate. Two parties, Blazing Cars Pte Ltd and Fiery Trucks Pte Ltd, wish to sign a
NDA to explore a business venture.

To track the effectiveness of our prompt, it's best to ask ChatGPT directly first. We will look at ChatGPT's output
and think about what we need to do to get the output we want.
"""

exercise_area("Exercise 5-1", default_text="Generate a Non-Disclosure agreement between Blazing Carts Pte Ltd "
                                           "and Fiery Trucks Pte Ltd", long=False)
"""
This looks fine, but it's no different from Googling and then copying a NDA. You wouldn't know if it is fit for purpose
or free of errors. Googling is also probably faster and cheaper too.

Let's make ChatGPT work harder.
"""

st.header("The steps to take to draft an NDA using ChatGPT")
"""
It's sometimes great and gratifying to be able to include all the information we want to provide the model in a 
single prompt. However, the goal of this exercise is to break this habit. In cases where we are not sure what is the
prompt we need to do the task, 
it might be useful to take advantage of the model's text generation ability as well as memory.

In order to make ChatGPT generate _our_ customised agreement, we have to take a few additional steps:

1. First we will ask ChatGPT what are the essential aspects of a NDA
2. Provide some information to give ChatGPT more context
3. Ask ChatGPT to generate the NDA using all the information provided. 

"""

st.subheader("Exercise 5-2: What are the essential aspects of a NDA?")
"""
Let's assume we are not familiar with what information we need to give ChatGPT to draft an NDA. 
As such, we need ChatGPT's help.
"""

exercise_area("Exercise 5-2", default_text="Blazing Carts Pte Ltd and Fiery Trucks Pte Ltd wish to conclude a non-"
                                           "disclosure agreement. As the parties' lawyer, what questions do you need "
                                           "to ask them to draft the agreement?",
              long=False)
"""
Now you have a list of questions ChatGPT can ask you to draft the agreement. By answering them, you can give 
ChatGPT more context to complete your agreement. 
"""

st.subheader("Exercise 5-3: Generate the NDA by answering the assistant's questions")
"""
Now we will need to build on the results of the previous query by giving ChatGPT the answers to the questions
it asked. Since we are going to use these answers to generate the agreement, ChatGPT needs to remember them, so we 
will "store" them in a form of a chat.  
"""

exercise_area("Exercise 5-3", exercise_type="chat",
              messages=[
                  {"role": "user", "content": "Blazing Carts Pte Ltd and Fiery Trucks Pte Ltd wish to conclude a non "
                                              "disclosure agreement. As the parties' lawyer, what questions do you "
                                              "need to ask them to draft the agreement?"},
                  {"role": "assistant", "content":
                      """1. What are the purposes for which the confidential information may be used?
2. How long will the agreement remain in force?
3. Will either party have the right to terminate the agreement, and if so, under what circumstances?
4. What will be the jurisdiction in the event of a dispute?
"""}])

"""
Now clarify ChatGPT's doubts by answering those questions. 
You can select a few questions, copy and paste the questions, then add the answers after each question. 
Finally, ask ChatGPT to produce the document. 
(You aren't limited to the list of questions provided by ChatGPT earlier/ You also don't have to answer every question
which ChatGPT generated.)  

If you'd like to quickly move on with the exercise, you can cut and copy the following response.

```
What are the purposes for which the confidential information may be used? To explore a new business venture.

How long will the agreement remain in force? 1 year

Will either party have the right to terminate the agreement, and if so, under what circumstances? Yes, by written agreement.

What will be the jurisdiction in the event of a dispute? Singapore.

Based on my answers, generate a Non disclosure agreement.
```

In the final line of my prompt, you can see that I have requested ChatGPT to generate a non-disclosure agreement.
If you have given it all the information you want, you should ask ChatGPT to generate the agreement already. 
You can use this prompt: `Based on my answers, generate a non-disclosure agreement.`

Check the NDA generated. Did it include the information you specified? If it did, you have generated your own
NDA!
"""

st.subheader("Bonus: Ownself Check Ownself")
"""
One of the pluckiest prompt engineering techniques is to ask ChatGPT to evaluate its answers. 
Go ahead, ask ChatGPT what it thinks about its own NDA in the previous exercise. 
You can experiment with the following prompts:

* Are there any missing aspects to the NDA?
* How can you improve on this NDA?

Once you have read ChatGPT's honest assessment of its work, you could try to include its comment in your NDA. 

... Or, you could ask ChatGPT to do it. Use this prompt "Using the above points, generate a new version of the NDA."

Now check the new NDA. Like all good robots, ChatGPT has taken its criticisms in its stride.  
"""

st.header("Conclusion")
"""
In this section, we used a step by step approach to improve both 
our inputs (we asked ChatGPT what questions we need to answer)
as well as our outputs (we asked ChatGPT to include more information or evaluate its answers). 
In doing so, we customised our non-disclosure agreement and made it better using the ChatGPT.

This gradual process of refining our inputs and outputs is necessary for prompt engineering. As every model is 
different, you will need some trial and error to get the best results. The most important lesson in this section
is that unexpectedly, your model is an excellent resource to help you use the model better. 
"""

with st.expander("This is a terribly risky way to generate an NDA: Generative AI vs Document assembly"):
    """
    Would you generate your non-disclosure agreement this way? A significant number of lawyers will be flabbergasted.
    
    There will be several arguments but I would like to focus on one: trust. 
    If ChatGPT took the template from a case where the NDA was the subject of a dispute, that is a 
    recipe for disaster.
    The point, though, is I don't know whether that is true or false. 
    This uncertainty will be enough for many lawyers to turn away from using ChatGPT to draft contracts.    
    If you're interested to read more about this topic, you can refer to this 
    [blog post](https://www.adamsdrafting.com/chatgpt-wont-fix-contracts/).
    
    The alternative is relatively of more vintage -- document assembly. Instead of having ChatGPT generate an 
    agreement using statistical probabilities, an expert designs an interview to get all the answers a computer
    agreement needs to generate an agreement. Today, you can write such a program using the open source 
    [docassemble](https://docassemble.org/) 
    platform. As the expert (who could be a lawyer) has more control over the product, this enhances trust in
    the program's output. 
    
    The best solution, in this author's opinion, may be combination of these technologies.   
    """

write_footer()
