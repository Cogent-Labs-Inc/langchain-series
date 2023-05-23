# Langchain-Series

The "langchain-series" project is a collection of diverse little apps that demonstrate the practical applications of AI chatbots in real-world scenarios. Each app within the series showcases the capabilities of chatbot technologies in different domains, providing users with interactive and engaging experiences.

## Installation

1. Clone the repository to your local machine:
2. Create a virtual environment using the following command:
    ```
    python3 -m venv your-env-name
    ```
3. Activate the virtual environment:
- On Linux or macOS:
  ```
  source env_name/bin/activate
  ```
- On Windows:
  ```
  env_name\Scripts\activate
  ```

4. Install the project dependencies by running the following command:
    ```
    pip install -r requirements.txt
    ```

## Setting Up Environment Variables

To use the project, you need to set up your environment variables. Follow the steps below to create a `.env` file in the base project directory and add your OpenAI API key.

1. Create a new file named `.env` in the base project directory.

2. Open the `.env` file in a text editor and add the following line:
```
OPENAI_API_KEY=your-api-key-goes-here
```
## Usage

1. Navigate to the project you want to run: `cd project_name`

2. Run the application using the following command:
  ```
  streamlit run app.py
  ```