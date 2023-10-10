# Quiz Generator for Educational Content

Quiz Generator is an app that utilizes Generative AI and the langchain library with OpenAI's gpt-3.5-turbo model to
create multiple-choice quizzes for educational content. The app takes a piece of text, the desired number of
multiple-choice questions, the target grade level, and the tone of the quiz as input. It then generates a set of
multiple-choice questions conforming to the given text and the specified criteria.

### Steps to Execute:

- Create the virtual environment using the command

`python -m venv env-name`

- Activate the virtual environment using the command

`source env-name/bin/activate`

- Navigate to the app directory

`cd 001_ed_tech_quiz/`

- Install the requirements using the command

`pip install -r requirements.txt`

- Run the Streamlit app

`streamlit run app.py`

- The app will open in your web browser, allowing you to interact with it.

Before running the Streamlit app, make sure to set the required environment variables, including the OPENAI_API_KEY in a
.env file.

### How it Works?

- The app reads input from the user, including a file (either a PDF or a text file) containing educational content, the
  number of multiple-choice questions to generate, the target grade level, and the tone of the quiz.
- It preprocesses the file content (text extraction from PDF or decoding from a text file) and prepares a prompt
  template for quiz generation using the langchain library.
- The prompt is then passed to the `gpt-3.5-turbo` model to generate the multiple-choice quiz based on the provided text
  and specifications.
- The app presents the generated quiz to the user in a tabular format, along with a review of the quiz's complexity and
  appropriateness for the specified grade level.

### POC Data

- The Proof of Concept (POC) data used in the app includes 5 multiple-choice questions and 3 students' data, carefully
  crafted to cover various scenarios and edge cases.

