import re
def first_word(text: str) -> str:
    """
        returns the first word in a given text.
    """
    list_text = re.findall(r"[a-zA-Z']+",text) # Remove characters that are not [a-zA-Z']
    return list_text[0]