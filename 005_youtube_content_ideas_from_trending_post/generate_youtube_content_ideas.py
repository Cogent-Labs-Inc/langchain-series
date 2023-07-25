import os

from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate
)

load_dotenv('.env')

chat = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))


def generate_youtube_ideas_from_content(page_content: dict) -> str:
    """
    Generates youtube ideas for the given content

    :param page_content: extracted title, description and comments/replies
    :return: generated ideas
    """
    human_message = f"""
    I've the following topic
    {page_content['title']}
    with the description
    {page_content['description']}
    And the following are the comments on that
    {page_content['comments']}
    
    Generate 5 different viral YouTube content ideas related to this. For each idea, please provide
    title, description and youtube content script (with timestamps)
    
    Output the result in the following format using markdown:
    
    Idea 1:
    Title:
    Description:
    YouTube content script(with timestamps):
    0:00 some script content
    0:30 other script content
    
    Idea 2:
    Title:
    Description:
    YouTube content script(with timestamps):
    0:00 some script content
    0:30 other script content

    ...
    """

    system_message_prompt = SystemMessagePromptTemplate.from_template("You are an expert youtube content creator.")
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_message)

    chat_prompt = ChatPromptTemplate.from_messages(
        [
            system_message_prompt,
            human_message_prompt
        ]
    )

    chat_model = ChatOpenAI(temperature=0.2, model="gpt-3.5-turbo-16k")

    llm_chain = LLMChain(prompt=chat_prompt, llm=chat_model)
    response = llm_chain.run(input=human_message)

    response = response.replace("\n", "\n\n")

    return response
