# Speech Synthesis

Speech Synthesis is a generative AI Streamlit app developed using Langchain, OpenAI apis, and ElevenLabs. It first
creates a podcast introduction in the style of ***Joe Rogan*** or ***Jordan Peterson***, according to user's choice.
After that, it performs speech synthesis on the podcast. There are around 40 options available for the podcast speech
synthesis.

### Steps to Execute:

- Create the virtual environment using the command

`python -m venv env-name`

- Activate the virtual environment using the command

`source env-name/bin/activate`

- Navigate to the app directory

`cd 004_speech_synthesis/`

- Install the requirements using the command

`pip install -r requirements.txt`

- Run the Streamlit app using

`streamlit run app.py`

Before running the app, create a `.env` file, containing the API keys, in the same format as `.env.example`

### How it Works?

- Gets the Podcast details (Title, Theme, Summary, Podcast style) from the user
- Generates podcast introduction in the selected style using Langchain
- Takes input for the speaker to perform speech synthesis in that voice
- Performs speech synthesis using ElevenLabs

### POC Data

- The app provides two options for Podcast style and only available voices in ElevenLabs to perform Speech Synthesis.