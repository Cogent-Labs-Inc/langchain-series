# YouTube Video Engagement Analyzer

YouTube Video Engagement Analyzer is an application developed to increase the engagement of YouTube videos by analyzing
the scripts of old videos. The app uses Generative AI and is built on the langchain framework, utilizing OpenAI's
`gpt-3.5-turbo` model. It generates new video ideas and themes based on the common patterns found in high-engagement
videos.

### Steps to Execute:

- Create the virtual environment using the command

`python -m venv env-name`

- Activate the virtual environment using the command

`source env-name/bin/activate`

- Navigate to the app directory

`cd 002_youtube_content_ideas_ai/`

- Install the requirements using the command

`pip install -r requirements.txt`

- Run the Jupyter Notebook

`jupyter notebook youtube_traction.ipynb`

Before running the Jupyter Notebook, create a `.env` file containing the `OPENAI_API_KEY`

### How it Works?

- The application fetches data from high-engagement YouTube videos and low-engagement YouTube videos.
- It splits the video scripts into smaller chunks using a text splitter.
- The summarizer module then runs these chunks through the GPT-3.5 Turbo model to generate summaries for each video.
- The application uses a thread pool executor to process multiple URLs simultaneously, enhancing efficiency.
- After generating summaries for high-engagement and low-engagement videos, the application formats the results and
  presents them in DataFrames.
- The application further prepares a prompt template to generate new ideas and themes for future videos. It uses the
  GPT-3.5 Turbo model again to generate at least 10 new ideas related to high-engagement videos while avoiding any
  content from low-engagement videos.

### POC Data

- For the proof of concept (POC), the application uses 5 high-engagement videos and 3 low-engagement videos. The data is
  structured to cover various scenarios and edge cases.