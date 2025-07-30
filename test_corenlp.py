from nlplogic.corenlp import search_wikipedia, summarize_wikipedia, get_textblob, get_phrases


def test_get_phrases() : 
    assert 'boot'  in get_phrases("Golden Boot Football")