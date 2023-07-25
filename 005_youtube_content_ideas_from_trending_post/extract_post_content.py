import lxml.html
import requests


def refactor_extracted_comments(comments: list) -> str:
    """
    Refactors and cleans the extracted comments

    :param comments: comments being parsed
    :return: refactored comments
    """
    comments = "".join(comments)
    lines = comments.split("\n")
    cleaned_lines = [line.strip() for line in lines]

    refactored_lines = [line for line in cleaned_lines if line]
    refactored_text = "\n".join(refactored_lines).replace("\n\n", "\n").replace("reply", "\nreply:")

    return refactored_text


def extract_page_content(url: str) -> dict:
    """
    Extracts the page content from the specified url

    :param url: url for which content is extracted
    :return: extracted page content
    """
    response = requests.get(url=url)

    page = lxml.html.fromstring(response.text)
    title_text = page.xpath("//span[@class='titleline']//a/text()")
    description_text = page.xpath("//div[@class='toptext']/text()")
    comments = page.xpath("//div[@class='comment']//descendant-or-self::*/text()")

    refactored_comments = refactor_extracted_comments(comments)

    return {
        "title": "".join(title_text),
        "description": "".join(description_text),
        "comments": refactored_comments
    }
