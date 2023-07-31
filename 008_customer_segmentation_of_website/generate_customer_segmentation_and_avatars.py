import os

from dotenv import load_dotenv
from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import SystemMessagePromptTemplate, HumanMessagePromptTemplate, ChatPromptTemplate


load_dotenv()

chat = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))


def generate_customer_segmentation_of_webpage_content(extracted_content):
    human_message = """
As an expert marketing analyst, your task is to create 5 attractive and impactful customer segments based on the 
website audience for the given webpage content that will appeal the audience to visit the webpage.

Webpage Content:
{page_content}

Consider the following instructions while creating customer segmentation:
Analyze the webpage content: To deeply understand the context of your webpage, carefully analyze its content. 
Use your research skills to identify the main themes, products, or services being offered.

Identify target audience: Identifying the target audience is a critical step for any business. Determine the type of 
audience that is likely to visit the webpage. Consider their demographics, interests, and pain points.

Now that you have insights into the potential customers visiting the webpage, generate 5 distinct customer segments 
based on their characteristics, behaviors, or interests. Group similar visitors together to form meaningful segments. 

Also generate 3 different avatars for each customer segment that have their name, age/range(years), location, 
occupation, income, education, pain points and goals.

Generate output in the following format:
Segment 1:
Name:
Description:
Key feature:
Avatars:

Segment 2:
Name:
Description:
Key feature:
Avatars:
and so on (create total 5 segments)

Also, generate output for each avatar in the following format:

Avatar 1:
Name:
Age/Range(years):
Location:
Occupation:
Income:
Education:
Pain points:
Goals:

Avatar 2:
Name:
Age/Range(years):
Location:
Occupation:
Income:
Education:
Pain points:
Goals:
and so on (must create 3 avatars for each customer segment)
"""

    system_template = "You are an expert marketing analyst"
    system_message_prompt = SystemMessagePromptTemplate.from_template(system_template)
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_message)

    chat_prompt = ChatPromptTemplate.from_messages(
        [
            system_message_prompt,
            human_message_prompt
        ]
    )

    chat_model = ChatOpenAI(temperature=0.8, model="gpt-3.5-turbo-16k")

    llm_chain = LLMChain(prompt=chat_prompt, llm=chat_model, verbose=True)
    response = llm_chain.run(page_content=extracted_content)
    response = response.replace("\n", "\n\n")

    return response
