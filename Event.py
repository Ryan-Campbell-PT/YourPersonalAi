import spacy
from spacy.matcher import Matcher
from Database import runDatabaseCommand, getDateFromEnt
from Model import getNlp

displayDebuggerInformation = True
attentionPhrase = "Hey Microphone, " #this should be a database entry

# an event should contain an event and the date

def debugger_textPrint(textToDisplay = "", addNewLine = False):
    if(displayDebuggerInformation):
        print(textToDisplay)

    if(addNewLine): print("\n\n")


def Main():
    eventCommands = [
        "I cleaned the bathroom today", #context for current date, event and location (clean, bathroom)
        "I ate out yesterday", #context for previous date, event (ate out)
        "I am going to water the plants tomorrow", #context for next date, event (water the plants)
        "I'm going to the movies on February 5th", #context for specific date, event and location (go to movies, movie)
        "I'm going to buy some groceries on the 12th", #context for generalized date, event (buy some groceries)
        "I just cleaned the bathroom", #no obvious context for date
        ]

    nlp = getNlp()

    for event in eventCommands:
        doc = nlp(attentionPhrase + event)

        for ent in doc.ents:
            print(getDateFromEnt(ent))
        # debugger_textPrint(textToDisplay="Text being parsed: " + doc.text)

        # for token in doc:
        #     debugger_textPrint("Token text: " + token.text)
        #     debugger_textPrint("Token ent type: " + token.ent_type_)
        #     debugger_textPrint("Token lemma: " + token.lemma_)
        #     debugger_textPrint("Token shape: " + token.shape_)
        #     debugger_textPrint("Token pos: " + token.pos_)
        #     debugger_textPrint("Token tag: " + token.tag_, True)
        # for ent in doc.ents:
        #     debuggerInfo("Event Text: " + ent.text)
        #     debuggerInfo("Event Label: " + ent.label_, addNewLine = True)


Main()