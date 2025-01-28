import spacy 
from spacy.matcher import Matcher

def getMatcher(nlp):
    matcher = Matcher(nlp.vocab)
    matcher = setMatcherPatterns(matcher)
    return matcher

def setMatcherPatterns(matcher):
    patterns = []
    patterns.append([
        {"POS": "VERB"},
        {"POS": "DET", "OP": "?"},
        {"POS": "NOUN"}
        ])
    patterns.append([
        {"POS": "VERB"},
        {"POS": "ADP"},
        # {"POS": "PART", "OP": "?"},
        # {"POS": "ADP", "OP": "?"},
        # {"POS": "DET", "OP": "?"},
        # {"POS": "NOUN", "OP": "?"}
        ])
    patterns.append([
        {"POS": "VERB"},
        {"POS": "ADP"},
        {"POS": "DET"},
        {"POS": "NOUN"}
    ])
    patterns.append([
        {"POS": "VERB"},
        {"POS": "DET"},
        {"POS": "PROPN"}
    ])
    patterns.append([
        {"POS": "VERB"},
        {"POS": "PRON"},
        {"POS": "NOUN"},
        {"POS": "NOUN"},
    ])
    
    matcher.add("EVENT", patterns)
    
    return matcher

