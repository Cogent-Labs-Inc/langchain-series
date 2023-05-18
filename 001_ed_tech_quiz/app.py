import json

from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SequentialChain
import streamlit as st
import PyPDF2
import traceback
from langchain.callbacks import get_openai_callback

load_dotenv()


def parse_file(file):
    if file.name.endswith('.pdf'):
        try:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()
            return text
        except PyPDF2.utils.PdfReadError:
            raise Exception("Error reading the PDF file.")

    elif file.name.endswith('.txt'):
        return file.read().decode('utf-8')

    else:
        raise Exception("Unsupported file format. Only PDF and TXT files are supported.")


# This is an LLMChain to create 10-20 multiple choice questions from a given piece of text.
llm = OpenAI(model_name='gpt-3.5-turbo', temperature=0, max_tokens=-1)

response_json = json.dumps({
    "1": {"no": "1", "mcq": "multiple choice question",
          "options": {"a": "choice here", "b": "choice here", "c": "choice here", "d": "choice here"},
          "correct": "correct answer"},
    "2": {"no": "2", "mcq": "multiple choice question",
          "options": {"a": "choice here", "b": "choice here", "c": "choice here", "d": "choice here"},
          "correct": "correct answer"},
    "3": {"no": "3", "mcq": "multiple choice question",
          "options": {"a": "choice here", "b": "choice here", "c": "choice here", "d": "choice here"},
          "correct": "correct answer"}
})

template = """
Text: {text}
You are an expert MCQ maker. Given the above text, it is your job to create a quiz of {number} multiple choice questions for grade {grade} students in {tone} tone.
Make sure that questions are not repeated and check all the questions to be conforming to the text as well.
Make sure to format your response like the RESPONSE_JSON below and use it as a guide. Ensure to make the {number} MCQs.
### RESPONSE_JSON
{response_json}
"""
quiz_generation_prompt = PromptTemplate(input_variables=["text", "number", "grade", "tone", "response_json"],
                                        template=template)
quiz_chain = LLMChain(llm=llm, prompt=quiz_generation_prompt, output_key="quiz", verbose=True)

# This is an LLMChain to evaluate the multiple choice questions created by the above chain
llm = OpenAI(model_name='gpt-3.5-turbo', temperature=0)
template = """You are an expert english grammarian and writer. Given a multiple choice quiz for {grade} grade students. You need to evaluate complexity of the questions and give a complete analysis of the quiz if the students 
will be able to understand the questions and answer them. Only use at max 50 words for complexity analysis.
If quiz is not at par with the cognitive and analytical abilities of the students, update the quiz questions which need to be changed and change the tone such that it perfectly fits the students abilities. 
Quiz MCQs:
{quiz}
Critique from an expert english writer of the above quiz:"""

quiz_evaluation_prompt = PromptTemplate(input_variables=["grade", "quiz"], template=template)
review_chain = LLMChain(llm=llm, prompt=quiz_evaluation_prompt, output_key="review", verbose=True)

# This is the overall chain where we run these two chains in sequence.
generate_evaluate_chain = SequentialChain(
    chains=[quiz_chain, review_chain],
    input_variables=["text", "number", "grade", "tone", "response_json"],
    # Here we return multiple variables
    output_variables=["quiz", "review"],
    verbose=True)

st.title('🦜⛓️ Langchain-Series: 001-Quiz Generation for Educational Content')

# Create a form using st.form
with st.form("user_inputs"):
    # File upload
    uploaded_file = st.file_uploader("Upload a pdf or text file")

    # Input fields
    mcq_count = st.number_input("No of MCQs", min_value=3, max_value=20)
    grade = st.number_input("Insert Grade", min_value=1, max_value=10)
    tone = st.text_input("Insert Quiz tone", max_chars=100, placeholder="simple")

    button = st.form_submit_button("Create quiz")

# Check if the button is clicked and all fields have inputs
if button and uploaded_file is not None and mcq_count and grade and tone:
    try:
        text = parse_file(uploaded_file)

        # count tokens and cost of api call
        with get_openai_callback() as cb:
            response = generate_evaluate_chain({
                "text": text,
                "number": mcq_count,
                "grade": grade,
                "tone": tone,
                "response_json": response_json
            })
    except Exception as e:
        st.error(traceback.print_exc())
    else:
        print(f"Total Tokens: {cb.total_tokens}")
        print(f"Prompt Tokens: {cb.prompt_tokens}")
        print(f"Completion Tokens: {cb.completion_tokens}")
        print(f"Total Cost (USD): ${cb.total_cost}")

    if isinstance(response, dict):
        try:
            # Extract quiz data from the response
            quiz_data_str = response.get("quiz", None)
            if quiz_data_str is not None:
                # convert the quiz from a str to dict
                quiz_dict = json.loads(quiz_data_str)
                quiz_table_data = []
                # Iterate over the quiz dictionary and extract the required information
                for key, value in quiz_dict.items():
                    mcq = value["mcq"]
                    options = " | ".join(
                        [f"{option}: {option_value}" for option, option_value in value["options"].items()])
                    correct = value["correct"]
                    quiz_table_data.append({"MCQ": mcq, "Choices": options, "Correct": correct})
                st.table(quiz_table_data)
                # Display the review in a text box
                st.text_area(label="Review", value=response['review'])
        except Exception as e:
            traceback.print_exc()
    else:
        st.write(response)
