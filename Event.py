import spacy
from spacy.tokens import Span, Doc, Token
from spacy.matcher import Matcher
from Database import saveEventToDB
from Model import getNlp

displayDebuggerInformation = True
attentionPhrase = "Hey Microphone, " #this should be a database entry

# an event should contain an event and the date

def debugger_textPrint(textToDisplay = "", addNewLine = False):
    if(displayDebuggerInformation):
        print(textToDisplay)

    if(addNewLine): print("\n\n")


def getEventFromText(doc: Doc):
    for ent in doc.ents:
        head: Token = ent.root.head # beginning of the event
        # should then grab a string until you get to the ent
        eventSpan = Span(doc, head.i, ent.start, "EVENT")
    #     print(f"Event Span: {eventSpan}")
    # print()
    return eventSpan

def Main():
    commands = [
        "I cleaned the bathroom today", #context for current date, event and location (clean, bathroom)
        "I ate out yesterday", #context for previous date, event (ate out)
        "I am going to water the plants tomorrow", #context for next date, event (water the plants)
        # "I'm going to the movies on February 5th", #context for specific date, event and location (go to movies, movie)
        # "I'm going to buy some groceries on the 12th", #context for generalized date, event (buy some groceries)
        # "I just cleaned the bathroom", #no obvious context for date
        # "Liz took a Benadryll last week", #no obvious context for date, establishes a proper noun that can be made generic like 'allergy medicine/meds'
        # "We got our covid19 vaccines in 2021", #no obvious context for date or person, requires keeping 'in 2021' as one phrase to match date
        # "I got my flu shots in February, covid too", #establishes multiple db entries for both covid and flu, has generic phrase 'covid', isnt obvous covid is even included in first phrase
        ]

    nlp = getNlp()
    
    for command in commands:
        # doc = nlp(attentionPhrase + event)
        doc = nlp(command)

        event = getEventFromText(doc)

        print(f"DB save success: {saveEventToDB(doc, event.text)}")
        
        # print([(token.text , token.pos_) for token in doc])
        # print([(ent.text, ent.root.head) for ent in doc.ents])

        # for ent in doc.ents:
        #     print(f"{ent.text}, {ent.root.head}")

        # print()

        # print([(token.ent_type_) for token in doc])
        # print([(ent.text, ent.start_char, ent.end_char) for ent in doc.ents])


# so my first thought process for this is find the verd, and take it till you find the date
# use whatever the noun is in that sentence to determine the action/database entry
# save the date which will be stored in the doc.ents
Main()