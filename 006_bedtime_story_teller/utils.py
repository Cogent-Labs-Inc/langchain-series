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
    chat = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

    system_message_prompt = SystemMessagePromptTemplate.from_template(
        """As a gifted author of bedtime stories for children, your tales consistently embody these captivating elements:
1. Intriguing climaxes and surprising anti-climaxes.
2. Thrilling adventures.
3. A series of engaging and challenging tasks for children.
4. Detailed descriptions of each task and the steps taken to accomplish them.
5. Stimulate problem-solving skills in young readers.
6. Introduce a multitude of imaginative creatures with varying powers.
7. Accompany the story with colorful illustrations to maintain interest and aid understanding.
8. Incorporate recurring sequences or phrases that soothe and reassure young listeners.
9. Engage young readers with elaborative descriptions that captivate their imagination.
10. Infuse positive affirmations throughout the story to encourage confidence and kindness.
11. Provide a heartwarming happy ending with valuable life lessons to inspire young minds.
12. Include a variety of problems with climaxes and anti-climaxes for added excitement.
13. Employ a pleasant tone that soothes the hearts and minds of young readers.
14. Demonstrate verbosity and innovation in storytelling to keep the narrative fresh and captivating.
"""
    )
    human_message_prompt = HumanMessagePromptTemplate.from_template(
        """Below are the profiles of two children:

{children_data}

Your enchanting task is to craft a mesmerizing detailed and descriptive bedtime story that contains these characters.
You must include each child's characteristics given in the above data, into the story.

Embrace the magic of storytelling and create a unique unforgettable innovative tale that imparts wisdom, ignites imagination, encourages action with tasks and problem solving, and leaves a lasting impression on their young hearts.
You must describe each task or adventure they accomplish in very detail. The story must be descriptive.
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
