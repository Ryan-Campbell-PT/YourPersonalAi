import spacy
from spacy.matcher import Matcher

# essentially the job of this class will have to be training the model
# to grab events from increasingly more natural way people communicate
## dates wont always be specified and identified cause you can say something like
## 'i just cleaned the bathroom' which from a parsing perspective doesnt contain anything to work with
## so you have to be able to write different ways to understand how events are presented to spaCy

### you may be able to train the model to recognize different ways dates are referenced
### so "February 15th" "the 15th" will have to be trained to be the same dates
def getNlp():
    return spacy.load("en_core_web_md")

def modelTraining():
    return
