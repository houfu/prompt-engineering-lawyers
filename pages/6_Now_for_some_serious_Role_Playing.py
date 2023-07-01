import streamlit as st

from helpers import use_custom_css, check_openai_key, write_footer
from prompt_widget import exercise_area, ExerciseType

st.set_page_config(
    page_title="Now for some serious role playing — Prompt Engineering for Lawyers",
    layout="wide"
)

use_custom_css()

check_openai_key()

st.title("Now for some serious role playing")
"""
Role playing is one of the most effective prompt engineering techniques available.

You role play when you instruct an LLM to "become" or "mimic" a particular role, job, or function. 
There have been several examples of this in the previous exercises:

* We asked the LLM to "write the email in the voice of a pirate lawyer" 
* We asked the LLM to play the part of John's lawyer to generate an opening statement in "Generating Text"
* In "Taking Steps", we asked the LLM to play the part of the parties' lawyers to draft an agreement

Role playing is helpful heuristic to encourage you to provide the LLM with more information and clear and concise
instructions. If you are new to prompt engineering, role playing will often improve the effectiveness
of your prompt. 

In this exercise, we will push role playing and explore its limits.
"""

st.subheader("Exercise 6-1: Enter ChatGPT J")
"""
In a courtroom, there are usually three sides - the judge and the lawyers representing both sides. 

In this exercise, we will simplify this scenario into just two sides - the judge and a lawyer. 
Basically, it's an _ex parte_ application for substituted service. 
Substituted service is a legal process by which a copy of legal documents, such as a summons or complaint, 
is served on a defendant in a lawsuit when personal service (physically handing the documents to the defendant) 
is not possible.

Let's get our hands wet by getting ChatGPT to role play the judge. In order to role play the judge, ChatGPT needs
to know something about how to grant substituted applications. For this we will copy the practice directions on
this subject from the courts in Singapore.

Finally, we need a submission from the lawyers. We are going to do that. 

Review the prompt below and let's see if ChatGPT will grant our application for substituted service. 
"""

exercise_area('Exercise 6-1',
              default_text="You are a judge in the Supreme Court of Singapore. These are the directions regarding "
                           "substituted service: \n\n"
                           "```\n"
                           "(1) In any application for substituted service, the applicant should persuade the Court "
                           "that the proposed mode of substituted service will probably be effectual in bringing the "
                           "document in question to the notice of the person to be served.\n"
                           "(2) Two reasonable attempts at personal service should be made before an application for "
                           "an order for substituted service is filed. In an application for substituted service, the "
                           "applicant shall demonstrate by way of affidavit why he or she believes that the attempts "
                           "at service made were reasonable.\n"
                           "(6) If substituted service is by electronic mail, it has to be shown that the electronic "
                           "mail account to which the document will be sent belongs to the person to be served "
                           "and that it is currently active.\n"
                           "```\n\n"
                           "I am a lawyer applying for substituted service. This is my submission:\n\n"
                           "```\n"
                           "Your honour, I am Mr X for the Plaintiff. This is an application for substituted service. "
                           "We wish to send the originating claim to the defendant by email. We humbly request to grant"
                           " the order. \n"
                           "```\n"
                           "What is your next line?",
              )
"""
For the rest of this exercise, I would be describing the steps to explore our ChatGPT judge ("ChatGPT J").

1. That was a tad presumptuous on our part. We provided some **context** on how ChatGPT J should decide the application.
It's now using that context to answer our question. Try to see if you can respond to ChatGPT J's feedback and convince 
him to grant our application. 
2. You might now find that ChatGPT J is a nightmare of a judge. You can't convince him to grant the order. Try to see if 
you can get him to do so by introducing an **objective** to ChatGPT J. You can add `If all the requirements are met, 
grant the order.` to ChatGPT J's instructions and see if it helps.
3. Let's make ChatGPT J a bigger nightmare. Let's give ChatGPT J a **personality**. He's now `irritable, impatient and 
does not tolerate any mistakes.` See how that affects ChatGPT J's responses.
4. To date, you might have noticed that ChatGPT J is nice enough to tell you to amend your submission if they are 
not sufficient. Give ChatGPT J **an option to respond if the requirements are not met**. For example, `if the 
application does not meet the directions, dismiss it.` 
Additionally you may also like ChatGPT J to abuse the lawyer for wasting the court's time.

I hope that when you followed the steps above, you get an idea of how you can improve the role play in your prompts. 
Such details provide the LLM with information on how to respond as you want. It helps at this juncture to be creative.
"""

st.subheader("Exercise 6-2: Enter ChatGPT OC")
"""
The previous exercise was an _ex parte_ application. Let's up the ante by having an opposing counsel contribute
to the arguing of your application. We will have two personalities in this chat, one for the judge and 
the opposing counsel.

In this exercise, your learned friend, ChatGPT OC, represents the plaintiff and has applied for an order of production
(previously known as a discovery order) against your client. See if you can oppose ChatGPT OC's application by
persuading ChatGPT J that the documents requested are not relevant to your case.

Due to the limitations of a single ChatGPT pretending to be two people at the same time, here are some hints to improve
your experience of this chat:

* If it's not your turn to speak, prompt ChatGPT to continue. For example, say `Go on, OC.`
* Depending on how ChatGPT's reads your response, it may terminate arguments. If you want to explicitly end arguments,
say `I have nothing further to add.` ChatGPT J will then render its decision.

"""

exercise_area('Exercise 6-2', ExerciseType.CHAT,
              messages=[
                  {
                      "role": "system",
                      "content": "This is a court in the Supreme Court of Singapore.\n"
                                 "These are the rules regarding an order for production of documents.\n"
                                 "```\n"
                                 "The Court may order any party to produce the original or a copy of a specific "
                                 "document or class of documents (called the requested documents) in the party’s "
                                 "possession or control, if the requesting party — (a)	properly identifies the "
                                 "requested documents; and (b)	shows that the requested documents are material to the "
                                 "issues in the case. \n"
                                 "```\n"
                                 "The Registrar represents the Court and will make the order if the rules are "
                                 "satisfied. He is professional and kind to the lawyers. "
                                 "When the Registrar says something, start with `[AR]`.  \n"
                                 "The applicant is represented by lawyer, ChatGPT OC, who is a wily and rude lawyer who"
                                 " is always trying to win the case at all costs. When ChatGPT OC says something, "
                                 "start with `[OC]`. \n"
                                 "Court hearing starts with OC making the submission, then I will make the rebuttal. "
                                 "Then generate a response to my rebuttal as OC."
                                 "Once I have nothing further to add, AR will make his decision by deciding "
                                 "whether the order should be given. \n\n"
                                 "Background: This is a claim for breach of employment contract. "
                                 "OC represents the Plaintiff, a pharmacy, which employed the Defendant. "
                                 "The Plaintiff alleges that the Defendant stole the Plaintiff's supplies, "
                                 "being medical drugs. \n\n"
                                 "Let's start."
                  },
                  {
                      "role": "assistant",
                      "content": "[OC] May it please the court. I represent the Plaintiff. I am applying for an "
                                 "order for the Defendant to produce all the emails exchanged between himself and his "
                                 "doctor. I believe it contains relevant information for my case."
                  }
              ])
"""
So, how did you fare? Did you beat ChatGPT by convincing ChatGPT to rule in your favour?

In the meantime, consider how the prompts were improved by adding context, objectives, personality and responses to 
failure. By adding these details, ChatGPT was able to creatively generate outputs that would suit your purpose.
"""

with st.expander("Simulated training for lawyers"):
    """
    Some people are concerned that the 
    [opportunities for young lawyers today to practice advocacy are shrinking](https://journalsonline.academypublishing.org.sg/Journals/SAL-Practitioner/Advocacy-and-Procedure/ctl/eFirstSALPDFJournalView/mid/589/ArticleId/1285/Citation/JournalsOnlinePDF)
    . Is this a cause for concern?
    
    If you enjoyed the exercises in this section, you might already know what the future might hold.
    Much like aircraft pilots, law students and lawyers can clock hours of trainings in "simulators" powered by LLMs. 
    While certain vaunted aspects of advocacy (such as following the judge's pen) might be impossible to teach in a
    chat setting, lawyers can still be exposed to a wide range of situations in simulated environments and can
    evaluate the effects of their actions without causing loss to the client (or anxiety to the lawyer). Clients also
    will not be forced to pay a law firm to train their young lawyers on their matters. 
    
    The idea of simulator trainings was also mentioned by Richard Susskind as a response towards the possible loss of 
    skills when work is displaced by smart systems. (See [The End of Lawyers](https://orreadi.com/book/26677/s/the-end-of-lawyers), 
    page 118)
    """


st.header("Conclusion")
"""
Role playing is an important technique to improve the effectiveness of your prompts. By focusing on all the aspects of 
the role that an LLM can play, it is possible to provide more information to the LLM to create diverse output. 

We also noted that there are other techniques to improve your prompts. 
In order for ChatGPT to play two roles, you have to set out the process and parameters for the LLM to respond 
to the different kinds of input it may encounter. So while you may get very far in
asking LLMs to "pretend" to be something, it is limited and may not even be necessary if the problem is not relevant to
the role an LLM can play. In this case, prompt engineering looks less like theatre productions or magic shows, 
and more like programming. 

From this point, prompt engineering looks less like English, and more like engineering. However, prompt engineering
is still easier to grasp for most people including lawyers because it is written in natural English. Hang on for the 
ride!  
"""

write_footer()
