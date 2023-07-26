# Viral Youtube Video Ideas Generator

It is a Generative AI Streamlit app that uses Langchain and OpenAI API to generate viral youtube ideas for the 
extracted content of Hacker news post.

## Stack Details
- Python = 3.10

### Steps to Execute:
- Create the virtual environment using the command
  ```
  python3 -m venv your-env-name`
  ```
  (replace `venv` with the name of virtual environment)

- Activate the virtual environment using the command
  ```
   source env_name/bin/activate
  ``` 
- Before installing the command navigate to the app directory. If you are outside the 
   directory execute the command
  ```
  cd 005_youtube_content_ideas_from_trending_post/`
  ```
- Install the requirements using the command
  ```
  pip install -r requirements.txt
  ```
- Execute the Streamlit app on local host using the command
  ```
  streamlit run main.py
  ```

### How it Works?
- When a user inputs url of Hacker news post, it extracts the page title, description, comments and replies of the post.
- A method refactors the extracted comments so that are understandable for LLM (Large Language Model).
- In the final step the extracted content is used to generate the prompt that is passed to the chat model, which in turn
  returns viral youtube ideas with their description and content script

### POC Data
- For the POC of getting viral youtube videos content we are using the url of a `Stripe alternative post` of Hacker news.
  
  `https://news.ycombinator.com/item?id=36811026`
  