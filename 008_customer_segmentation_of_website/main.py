import streamlit as st

from extract_website_content import extract_website_content
from generate_customer_segmentation_and_avatars import generate_customer_segmentation_of_webpage_content


def main():
    st.title("Customer Segmentation and Avatars Generator")

    url = st.text_input("Enter the URL:")

    if url:
        with st.spinner("Processing..."):
            loader_placeholder = st.empty()

            page_content = extract_website_content(url)
            response = generate_customer_segmentation_of_webpage_content(page_content)

            loader_placeholder.empty()

            st.write(response)
    else:
        st.warning("Please enter a URL first.")


if __name__ == "__main__":
    main()
