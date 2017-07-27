"""This module contains functions used for defining word meaning."""

import synthesizer as synth

import requests
import bs4

DEFINE_EXPRESSIONS = (
    "define",
    "what is",
    "who is"
)

WIKIPEDIA_URL_BASE = "https://en.wikipedia.org/w/index.php?search="

def findwiki(expression):
    """This function finds the definition of an expression on Wikipedia"""
    result = requests.get(WIKIPEDIA_URL_BASE + expression.replace(" ", "+"))

    # Check for OK HTTP code
    if result.status_code == 200:
        # Return the text content of the page
        return result.content
    # Something has failed
    else:
        return None

def extract_def(wikipage):
    """This function extracts the defnition of the expression from a Wikipedia web page."""
    soup = bs4.BeautifulSoup(wikipage, "lxml")
    content_div = soup.find("div", {"class":"mw-parser-output"})
    first_paragraph = content_div.find("p", recursive=False).text

    # Remove citation markers
    for i in range(1, 10):
        first_paragraph = first_paragraph.replace("[%i]" % (i), "")

    return first_paragraph

def define(text):
    """This function performs the definition of the input expression."""
    subject = None

    # Remove the definition request portion of the input string
    for expr in DEFINE_EXPRESSIONS:
        if text.startswith(expr):
            if len(text) > len(expr):
                subject = text[len(expr):]
            break

    if subject:
        wikipage = findwiki(subject)
        synth.speak(extract_def(wikipage))

def is_define_request(text):
    """This function determines whether the input string is a definition request."""
    for expr in DEFINE_EXPRESSIONS:
        if text.startswith(expr):
            return True

    return False
