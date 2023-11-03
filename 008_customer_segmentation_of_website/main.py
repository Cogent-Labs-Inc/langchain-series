import streamlit as st

from extract_website_content import extract_website_content
from generate_customer_segmentation_and_avatars import generate_customer_segmentation_of_webpage_content


def main():
    st.title("Customer Segmentation and Avatars Generator")

    url = st.text_input("Enter the URL:")

    if url:
        with st.spinner("Extracting Page Content..."):
            page_content = extract_website_content(url)

        if page_content:
            with st.spinner("Generating Customer Segmentation..."):
                response = generate_customer_segmentation_of_webpage_content(page_content)

            st.write(response)
        else:
            st.warning("Invalid URL or some unknown error occurred")
    else:
        st.warning("Please enter a URL first.")


if __name__ == "__main__":
    main()
