# Viral Youtube Video Ideas Generator

It is a Generative AI task that uses Langchain and OpenAI API to generate viral youtube ideas with their content script.
It is a task that is deployed inside Streamlit app. Streamlit is an open-source Python library that is designed for 
creating web applications with simple and intuitive user interfaces for data science and generative AI projects.

### Prerequisites
Before running the Streamlit app make sure to install the requirements of the task from the requirements 
file of the directory. To install the requirements execute the command to enter the specific directory

`cd 005_youtube_content_ideas_from_trending_post/`

then after that run the command to install the requirements 

`pip install -r requirements.txt`

### How it Works?
- When a user inputs url of Hacker news post, It takes in url, pass it to the method to 
  extract the page title, description, comments and replies of the post.
- A method refactors the extracted comments so that are easy for LLM (Large Language Model) to understand.
- In the final step the extracted content i.e title, description, comments and replies has been passed to the method, 
  which takes them to generate a prompt and pass it to chat model to get viral youtube ideas content as response.

### How to Run Streamlit App:
- To execute the Streamlit app on localhost and execute the command

  `streamlit run main.py`

  (make sure to be inside the directory `005_youtube_content_ideas_from_trending_post/` before executing the command)
- Input the url `https://news.ycombinator.com/item?id=36811026` to get the viral YouTube ideas related to 
  stripe alternatives.
