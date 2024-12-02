from deep_translator import GoogleTranslator
import spacy

nlp = spacy.load("en_core_web_sm")

latvian_text = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte."

translated_text = GoogleTranslator(source='lv', target='en').translate(latvian_text)

doc = nlp(translated_text)

entities = {"Person Names": [], "Organizations": []}

for ent in doc.ents:
    if ent.label_ == "PERSON":
        entities["Person Names"].append(ent.text)
    elif ent.label_ == "ORG":
        entities["Organizations"].append(ent.text)

print("Recognized entities:")
print("Person Names:", entities["Person Names"])
print("Organizations:", entities["Organizations"])

# LOSES PERSONS NAMES
# translated_entities = {
#     "Person Names": [GoogleTranslator(source='en', target='lv').translate(name) for name in entities["Person Names"]],
#     "Organizations": [GoogleTranslator(source='en', target='lv').translate(org) for org in entities["Organizations"]],
# }

# print("Recognized entities:")
# print("Person Names:", translated_entities["Person Names"])
# print("Organizations:", translated_entities["Organizations"])
