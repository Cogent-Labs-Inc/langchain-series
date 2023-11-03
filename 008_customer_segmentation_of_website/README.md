# Customer Segmentation and Avatars Generator

It is a Generative AI Streamlit app that uses Langchain and OpenAI API to create customer segmentation and generate
avatars against each customer segment.

## Stack Details

- Python = 3.10

### Steps to Execute:

- Create the virtual environment using the command
  ```
  python3 -m venv your-env-name`
  ```
- Activate the virtual environment using the command
  ```
   source env_name/bin/activate
  ``` 
- Navigate to the app directory
  ```
  cd 008_customer_segmentation_of_website`
  ```
- Install the requirements using the command
  ```
  pip install -r requirements.txt
  ```
- Execute the Streamlit app on local host using the command
  ```
  streamlit run main.py
  ```
- Before running the streamlit app, create a `.env` file containing the `OPENAI_API_KEY`

### How it Works?

- When a user inputs url of a webpage, it extracts the page content.
- In the second step the extracted content is used to generate the prompt, which is passed to the chat model,
  which in turn returns customer segmentations along with their avatars

### POC Data:

For the POC, we are creating 5 customer segments and 3 avatars against each customer segment.