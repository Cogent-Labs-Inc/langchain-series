import re
from langchain.document_loaders import WebBaseLoader


def extract_website_content(url):
    loader = WebBaseLoader(url)

    data = loader.load()
    cleaned_text = re.sub(r'\n\s*\n', '\n\n', data[0].page_content)

    return cleaned_text
