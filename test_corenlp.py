from nlplogic.corenlp import get_phrases


def test_get_phrases() : 
    assert 'boot'  in get_phrases("Golden Boot Football")