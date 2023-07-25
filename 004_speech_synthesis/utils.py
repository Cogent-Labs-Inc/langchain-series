from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from elevenlabs import generate, Voice, voices
import streamlit as st
import os


def generate_intro(topic, theme, summary, show):
    prompt_template = """ As an expert writer, your task is to create an introduction for a captivating podcast that will leave \
the listeners spellbound and eager to explore more. Your audience is diverse, and your words should resonate with \
their curiosity, emotions, and interests. Following are the steps to guide you in crafting the perfect introduction:

TOPIC: {topic}

THEME: {theme}

SUMMARY: {summary}

Looking at above TOPIC, THEME and SUMMARY, your mission is to weave a magical introduction in the style of {show} that effortlessly draws \
the listeners into the heart of the narrative. The introduction must be engaging, \
thought-provoking, and leave an indelible mark on the minds of those who tune in.

Consider the following guidelines while composing your introduction:
Begin with a captivating hook: Capture the audience's attention right from the start with a mesmerizing opening line \
that sparks curiosity and creates an irresistible urge to explore further.

Set the tone: Infuse the introduction with an appropriate tone that complements the podcast's theme, \
be it mysterious, uplifting, nostalgic, or thrilling.

Paint vivid mental images: Use your mastery of language to create beautiful visualizations and \
paint a world that lures listeners into the realms of the podcast's subject matter.

Appeal to emotions: Connect with the audience's emotions by incorporating elements that evoke \
empathy, excitement, wonder, or even nostalgia.

Unveil the essence: While keeping the mystery alive, provide a glimpse of what the podcast entails, \
leaving the listeners yearning for more insights and revelations.

Embrace diversity: Ensure your writing is inclusive, relatable, and appeals to a broad range \
of audiences, transcending age, culture, and background.

Be concise yet impactful: Craft a concise introduction that leaves a lasting impact, \
making every word count towards creating an enchanting experience.
Embrace your role as an expert writer, and let your creativity and linguistic prowess shine through \
in this introductory piece. Never break your character. The Introduction must be \
300 words at max. The podcast introduction must be in style of {show}.

Introduction:
    """
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.1)
    PROMPT = PromptTemplate(
        template=prompt_template,
        input_variables=["topic", "theme", "summary", "show"],
    )
    chain = LLMChain(llm=llm, prompt=PROMPT, verbose=True, output_key="introduction")

    response = chain({"topic": topic, "theme": theme, "summary": summary, "show": show})
    return response.get("introduction")


def generate_audio(intro, voice):
    return generate(text=intro, voice=voice, model="eleven_monolingual_v1")


def get_image_path(speaker):
    image_path = f"./images/{speaker.lower().replace(' ', '-')}-profile.jpg"
    if os.path.exists(image_path):
        return image_path
    else:
        return None

@st.cache_data(show_spinner=False)
def get_voices():
    speakers = [voice.name for voice in voices()]
    speakers.insert(0, "")
    return speakers


def get_voice_by_name(name):
    return [voice for voice in voices() if voice.name == name][0]
