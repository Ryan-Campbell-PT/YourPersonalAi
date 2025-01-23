import spacy

# a PR record should contain a date, an activity (bench,squat), and a number associated with the activity
# maybe even reps along with weight??? (at that point its just easier to write down in an excel sheet)
def getPersonalRecordLanguage():
    # need to understand PR and record and personal record
    # also include language for 'max' and 'my best'
    prText = [
        "I set a bench press PR today of 185 pounds!",
        "Yesterday at the gym I maxed out the bench press at 185",
        "I squatted 220 today, the most I've ever done",
        "My bench press personal record is 185 pounds",
        "My best squat was 220 pounds"
    ]

    return prText

