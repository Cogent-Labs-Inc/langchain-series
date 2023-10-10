import streamlit as st
from dotenv import load_dotenv

from utils import generate_child_fields, get_voice_by_name, generate_audio, generate_bedtime_story

load_dotenv()


def main():
    st.title("Bedtime Story Generator")

    st.write(
        "Please enter the details about the children to create a bedtime story."
    )

    child_1_details = generate_child_fields(1)

    child_2_details = generate_child_fields(2)

    st.write("Further details")
    children_relation = st.text_input("Relation between children*")

    children_data = {
        "children": [child_1_details, child_2_details],
        "relation between children": children_relation,
    }

    required_fields_filled = all(child_data is not None for child_data in children_data["children"])

    if st.button("Generate Bedtime Story") and required_fields_filled and children_relation:
        st.subheader("Bedtime Story")

        with st.spinner("Processing..."):
            st.session_state.bedtime_story = generate_bedtime_story(children_data)

    if "bedtime_story" in st.session_state:
        st.write(st.session_state.bedtime_story)
        speaker_type = st.selectbox("Select the Speaker Voice Type", ["Male", "Female"])

        if st.button("Generate Audio"):
            speaker = "Thomas" if speaker_type == "Male" else "Dorothy"

            with st.spinner("Getting Voice from ElevenLabs..."):
                speaker_voice = get_voice_by_name(speaker)

            with st.spinner("Generating audio..."):
                audio_bytes = generate_audio(st.session_state.bedtime_story, speaker_voice)

            if audio_bytes:
                st.success("Audio Generated")
                st.audio(audio_bytes, format="audio/wav")

    else:
        st.warning("Please fill in all the required fields before generating the bedtime story.")


if __name__ == "__main__":
    main()
