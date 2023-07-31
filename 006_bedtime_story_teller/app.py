import streamlit as st

from utils import generate_bedtime_story, generate_child_fields


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

    # Check if all required fields are filled before generating the bedtime story
    required_fields_filled = all(child_data is not None for child_data in children_data["children"])

    if st.button("Generate Bedtime Story") and required_fields_filled and children_relation:
        st.subheader("Bedtime Story")

        with st.spinner("Processing..."):
            bedtime_story = generate_bedtime_story(children_data)
            st.write(bedtime_story)
    else:
        st.warning("Please fill in all the required fields before generating the bedtime story.")


if __name__ == "__main__":
    main()
