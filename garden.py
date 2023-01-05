# Import NPL library
import spacy

# Load the spacy model
nlp = spacy.load("en_core_web_sm")

# Define the list of garden path sentences
gardenpathSentences = [
    "Is Biden’s stolen election claim by Republicans true?",
    "Is the fact that Roger Federer is well known by the public?",
    "The author wrote the novel 'Lord of the Rings' was likely to be a best-seller.",
    "The tycoon sold the offshore oil tracts for a lot of money wanted to kill JR",
    "The cotton clothing is usually made of grows in Mississippi."
]

# Iterate over each sentence and perform entity recognition. It prints the results. 
for sentence in gardenpathSentences:
    doc = nlp(sentence)
    
    print("Sentence:", sentence)
    print("Entities:")
    for entity in doc.ents:
        print("\t", entity.text, entity.label_)
    print()

"""
Two unsual entities found within the sentences:
1) JR: This one was recognised with the label org, the sentence was found online to contextually I am not able to confirm 
it was meant to refer to the name or acronym of an existing instiution. 
2) Missisipi: This is obviously a location in the United States. It brings up the label GPE which interestingly is assigned
to geopolitical entities, i.e. countries, cities, states. 
"""