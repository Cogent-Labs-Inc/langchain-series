from utils import (
    generate_intro,
    generate_audio,
    get_image_path,
    get_voices,
    get_voice_by_name,
)
import streamlit as st
from dotenv import load_dotenv


load_dotenv()


def main():
    st.markdown(
        "<h1 style='text-align: center;'><b>Speech Generator</b></h1>",
        unsafe_allow_html=True,
    )

    # Create a form with three input fields
    with st.form("intro_form"):
        topic = st.text_input("Topic (Max 300 characters)", max_chars=300)
        theme = st.text_area("Theme")
        summary = st.text_area("Summary")
        show = st.selectbox(
            "Select podcast style",
            ["The Joe Rogan Experience", "The Jordan B. Peterson Podcast"],
        )
        
        generate_intro_button = st.form_submit_button("Generate Intro")

        if generate_intro_button and all([topic, theme, summary, show]):
            with st.spinner("Generating Intro..."):
                # Call the function to generate the intro and get the output
                podcast_intro = generate_intro(topic, theme, summary, show)
                st.session_state.podcast_intro = podcast_intro
        elif generate_intro_button and not all([topic, theme, summary, show]):
            st.warning("Fill all the above fields.")

    if "podcast_intro" in st.session_state:
        podcast_intro = st.session_state.podcast_intro
        st.header("Podcast Introduction")
        st.write(podcast_intro)

    if "selected_speaker" not in st.session_state:
        st.session_state.selected_speaker = ""

    if "podcast_intro" in st.session_state:
        st.header("Speech Synthesis")
        speakers = get_voices()
        speaker = st.selectbox("Select a Speaker", speakers, index=0)

        # Create a button "Create" to generate audio
        if speaker and speaker != "":
            st.session_state.selected_speaker = speaker
            speaker_image_path = get_image_path(speaker)
            if speaker_image_path:
                st.image(speaker_image_path, caption=speaker, use_column_width=True)
            with st.spinner("Getting Voice from ElevenLabs..."):
                speaker_voice = get_voice_by_name(speaker)
            with st.spinner("Generating audio..."):
                audio_bytes = generate_audio(podcast_intro, speaker_voice)
            if audio_bytes:
                st.success("Audio Generated")
                st.audio(audio_bytes, format="audio/wav")
        else:
            st.error("Speaker name must be selected")


if __name__ == "__main__":
    main()
