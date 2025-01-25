import spacy 
from spacy.matcher import PhraseMatcher

def defineMatcher():
    #simple example of loading patterns from file
    ruler = nlp.add_pipe("entity_ruler").from_disk("./patterns.jsonl")
    return