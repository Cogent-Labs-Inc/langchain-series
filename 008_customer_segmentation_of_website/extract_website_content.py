import re
from langchain.document_loaders import WebBaseLoader


def extract_website_content(url):
    error_code = "403 Forbidden"
    cleaned_text = None

    loader = WebBaseLoader(url)
    data = loader.load()

    if data[0].metadata['title'] != error_code:
        cleaned_text = re.sub(r'\n\s*\n', '\n\n', data[0].page_content)

    return cleaned_text
