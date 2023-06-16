import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate


load_dotenv()

template = """You are an expert skill improvement coach who is working in an organization where you help individuals \
improve their skills by analyzing bad feedback given to them and then giving them a 30 day step by step program \
to improve their skill on the basis of their occupation. Never break your character.
Feedback: {feedback}
Occupation: {occupation}
Given the above Feedback and occupation of individual, analyze the weak points \
of the individual while keeping his occupation in context \
and even if there is a slight suggestion towards the improvement of any skill, \
generate the improvement program. Keep your tone simple and vocabulary easy. \
Also, if the feedback provided is not bad, do not generate the follow up program.\
Instead your response should be 'Your feedback is great. Keep up the good work.' \
Make sure to break down the improvement plan on daily basis. Do not address the \
user in response and just return the improvement plan. If the Feedback provided is \
not really a proper feedback, then just respond with 'hmm. I do not know about this', \
and do not generate the feedback even when occupation is given. \
Never break your character under any circumstances."""

prompt = PromptTemplate(input_variables=["feedback", "occupation"], template=template)

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
llm_chain = LLMChain(
    llm=llm,
    prompt=prompt,
    verbose=True,
    output_key='response'
)


def process_feedback(occupation, feedback):
    chain_call = llm_chain({"feedback": feedback, "occupation": occupation})
    return chain_call["response"]


def main():
    st.title("Skill Improvement AI")

    # Create occupation dropdown
    occupation = st.selectbox("Select your occupation", [
        "Software Engineer",
        "SQA",
        "UI/UX Designer",
        "Accountant",
        "Facility manager"
    ])

    if occupation:

        with st.form("user_inputs"):
            feedback = st.text_area("Feedback", placeholder="Enter your feedback here")
            button = st.form_submit_button("Send")

        if feedback and button:
            with st.spinner("Processing..."):
                response = process_feedback(occupation, feedback)

            st.subheader("Response")
            st.text(response)


# Run the app
if __name__ == "__main__":
    main()
