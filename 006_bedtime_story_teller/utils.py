import os

import streamlit as st
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)


def generate_bedtime_story(children_data):
    load_dotenv()
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
    chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5)

    system_message_prompt = SystemMessagePromptTemplate.from_template(
        """You are a good bedtime story writer for children.
        Your stories always have the following characteristics:
        1. Valuable life lessons for children
        2. Include imaginative elements
        3. Adventures
        4. Include a quest with some task or problem to be solved
        5. Descriptive in nature for children
        6. Have positive affirmations
        7. Happy ending
        8. Relatively short and concise
        """
    )
    human_message_prompt = HumanMessagePromptTemplate.from_template(
        """The following are the details about some children
        {children_data}
        
        Your task is to write a bedtime story involving these children as characters. You must incorporate the 
        children's different characteristics specified as key value pairs in the above data into the story. The 
        characteristics include age, interests, hobbies, super powers they want, dream destination, challenges/fears, 
        the best person in their life, their favorite movie/book, pet, color and food."""
    )
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    chain = LLMChain(llm=chat, prompt=chat_prompt, verbose=True)

    response = chain.run(children_data=children_data)
    return response


def generate_child_fields(child_number):
    st.subheader(f"Child {child_number} Details")
    name = st.text_input(f"Name {child_number}*")
    gender = st.selectbox(f"Gender {child_number}*", ["Male", "Female"])
    age = st.number_input(f"Age {child_number}*", min_value=1, max_value=100)
    interests = st.text_area(f"Interests {child_number} (separated by commas)*")
    superpowers = st.text_area(f"Superpowers loved {child_number} (separated by commas)*")
    challenges_fears = st.text_input(f"Challenges/Fears {child_number}*")

    dream_destination = st.text_input(f"Dream Destination {child_number}")
    hobbies = st.text_area(f"Hobbies/Activities {child_number} (separated by commas)")
    best_person_name = st.text_input(f"Best person name {child_number}")
    best_person_relation = st.text_input(f"Best person relation {child_number}")
    favorite_book_movie = st.text_input(f"Favorite Book/Movie {child_number}")
    favorite_pet = st.text_input(f"Favorite pet {child_number}")
    favorite_food = st.text_input(f"Favorite Food {child_number}")
    favorite_color = st.text_input(f"Favorite Color {child_number}")

    required_fields = [name, gender, age, interests, superpowers, challenges_fears]
    if not all(required_fields):
        return None

    return {
        "Name": name,
        "Gender": gender,
        "Age": age,
        "Interests": interests.split(","),
        "Superpowers loved": superpowers.split(","),
        "Best person name": best_person_name,
        "Best person relation": best_person_relation,
        "Favorite pet": favorite_pet,
        "Hobbies/activities": hobbies.split(","),
        "Favorite Food": favorite_food,
        "Favorite Color": favorite_color,
        "Favorite Book/Movie": favorite_book_movie,
        "Dream Destination": dream_destination,
        "Challenges/Fears": challenges_fears,
    }
