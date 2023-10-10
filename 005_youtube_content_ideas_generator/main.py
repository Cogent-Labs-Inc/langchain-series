import streamlit as st

from extract_post_content import extract_hackernews_page_content
from generate_youtube_content_ideas import generate_youtube_ideas_from_content


def main():
    """
    Function to execute the script
    """
    st.title("Youtube Viral Video Ideas Generator")

    url = st.text_input("Enter the URL:")

    if url:
        with st.spinner("Processing..."):
            page_content = extract_hackernews_page_content(url)
            response = generate_youtube_ideas_from_content(page_content)

            st.markdown(response)
    else:
        st.warning("Please enter a URL first.")


if __name__ == "__main__":
    main()
