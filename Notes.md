## Knowledge I don't want to keep looking up

### #Token properties
`token.lemma_` - the base form of a word
	cooking->cook
	cleaning->clean
`token.ent_type_` - a descriptive entity (not all words are an `ent`)
	ORG->proper noun
	DATE
	PERSON
`token.pos_` - descriptor of a word
	PUNCT - punctuation
	PROPN - proper noun
	VERB
	DET - natural language word (for, the, a)


### #Ent types
Entire list can be found on their #Github https://github.com/explosion/spaCy/blob/master/spacy/glossary.py


### Links I dont want to bookmark
[Matcher Explorer](https://demos.explosion.ai/matcher)
[Span](https://spacy.io/api/span#attributes)


## Personal Notes
Something to keep in mind: When saving something to the DB as "Going to the movies",
grabbing that information back will require a different form of speech "When was the last time I was at the movies".
To grab that information from the DB will require a different query phrase that may require more work than expected