# Bedtime Storyteller

Bedtime storyteller is a generative AI Streamlit app developed using Langchain, OpenAI apis, and ElevenLabs. It creates
bedtime stories for children according to their specific requirements. The stories are designed in such a way that the
children are part of the story and the story reflects their interests befittingly.

### Steps to Execute:

- Create the virtual environment using the command

`python -m venv env-name`

- Activate the virtual environment using the command

`source env-name/bin/activate`

- Navigate to the app directory

`cd 006_bedtime_story_teller/`

- Install the requirements using the command

`pip install -r requirements.txt`

- Run the Streamlit app using

`streamlit run app.py`

### How it Works?

- Gets the children data from the user
- Generates a customized bedtime story using Langchain
- Generates audio form of the story with ElevenLabs

### POC Data

- The app is designed for two children, for the POC.