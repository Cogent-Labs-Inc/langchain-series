from utils import generate_intro, generate_audio, VOICE_ID_MAPPING, play_and_save_file
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

        all_fields_filled = topic and theme and summary
        generate_intro_button = st.form_submit_button("Generate Intro")
        
        
        if generate_intro_button and all_fields_filled:
            with st.spinner("Generating Intro..."):
                # Call the function to generate the intro and get the output
                podcast_intro = generate_intro(topic, theme, summary)
                st.header("Podcast Introduction")
                st.write(podcast_intro)
                st.session_state.podcast_intro = podcast_intro
        elif generate_intro_button and not all_fields_filled:
            st.warning("Fill all the above fields.")
        
    if "podcast_intro" in st.session_state:
        podcast_intro = st.session_state.podcast_intro
        
        st.header("Speech Synthesis")
        speaker = st.selectbox(
            "Select a Speaker", ["", "Joe Rogan", "Morgan Freeman", "Jordan Peterson"], index=0
        )

        # Create a button "Create" to generate audio
        if speaker and speaker !="":
            voice_id = VOICE_ID_MAPPING.get(speaker)
            with st.spinner("Generating audio..."):
                # Call the function to generate audio and get the audio file URL
                audio = generate_audio(podcast_intro[:300], voice_id )
            if audio:
                st.success("Audio Generated")
            
            file_name = 'audio'
        
            play_and_save_file()
    else:
        pass

if __name__ == "__main__":
    main()
