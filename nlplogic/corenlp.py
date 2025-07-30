from textblob import TextBlob
import wikipedia


def search_wikipedia(name):
    """
    Search Wikipedia for a given name."""

    print(f"search for {name} ")
    return wikipedia.search(name)


def summarize_wikipedia(name):
    """summarize wikipedia"""

    print(f"finding the summary for a given : {name} on wikipedia")
    return wikipedia.summary(name)


def get_textblob(text):
    """Get TextBlob  objet and returns ."""

    blob = TextBlob(text)
    return blob


def get_phrases(name):
    """Find wikipedia name and return back phrases"""

    # on recupère le summary
    text = summarize_wikipedia(name)
    blob = get_textblob(text)
    phrases = blob.noun_phrases

    return phrases
