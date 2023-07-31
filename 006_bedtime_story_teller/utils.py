import os

import streamlit as st
from elevenlabs import voices, generate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)


def generate_bedtime_story(children_data):
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
    chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.6)

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

Your task is to write a bedtime story involving these children as characters. 

You must incorporate all of the children's characteristics, given in the above data, into the story.
The characteristics are 
1. interests
2. hobbies
3. super powers they want
4. dream destination
5. challenges/fears
6. the best person in their life
7. favorite food
8. favorite movie/book
"""
    )
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    chain = LLMChain(llm=chat, prompt=chat_prompt, verbose=True)

    response = chain.run(children_data=children_data)
    return response


def generate_child_fields(child_number):
    st.subheader(f"Child {child_number} Details")
    name = st.text_input(f"C{child_number}. Name*")
    gender = st.selectbox(f"C{child_number}. Gender*", ["Male", "Female"])
    age = st.number_input(f"C{child_number}. Age*", min_value=1, max_value=100)
    interests = st.text_area(f"C{child_number}. Interests (separated by commas)*")
    superpowers = st.text_area(f"C{child_number}. Superpowers loved (separated by commas)*")
    challenges_fears = st.text_input(f"C{child_number}. Challenges/Fears*")

    dream_destination = st.text_input(f"C{child_number}. Dream Destination")
    hobbies = st.text_area(f"C{child_number}. Hobbies/Activities (separated by commas)")
    best_person_name = st.text_input(f"C{child_number}. Best person name")
    best_person_relation = st.text_input(f"C{child_number}. Best person relation")
    favorite_book_movie = st.text_input(f"C{child_number}. Favorite Book/Movie")
    favorite_food = st.text_input(f"C{child_number}. Favorite Food")

    required_fields = [name, gender, age, interests, superpowers, challenges_fears]
    if not all(required_fields):
        return None

    return {
        "Name": name,
        "Gender": gender,
        "Age": age,
        "Interests": interests.split(","),
        "Superpowers loved": superpowers.split(","),
        "Dream Destination": dream_destination,
        "Challenges/Fears": challenges_fears,
        "Hobbies/activities": hobbies.split(","),
        "Best person name": best_person_name,
        "Relation with best person": best_person_relation,
        "Favorite Food": favorite_food,
        "Favorite Book/Movie": favorite_book_movie,
    }


@st.cache_data(show_spinner=False)
def get_voice_by_name(name):
    return next((voice for voice in voices() if voice.name == name), None)


def generate_audio(intro, voice):
    return generate(text=intro, voice=voice, model="eleven_monolingual_v1")
