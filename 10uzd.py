from transformers import pipeline

translator = pipeline("translation", model="Helsinki-NLP/opus-mt-lv-en")

latvian_sentences = [
    "Labdien! Kā jums klājas?",
    "Es šodien lasīju interesantu grāmatu."
]

for sentence in latvian_sentences:
    translated = translator(sentence, max_length=40)
    print(f"Latviešu: {sentence} \nAngļu: {translated[0]['translation_text']}\n")
