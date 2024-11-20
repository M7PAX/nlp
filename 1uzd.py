import spacy
from collections import Counter

nlp = spacy.load("en_core_web_sm")

text = '''Šeit ir dots teksts:  
"Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."'''
doc = nlp(text)

word_count = Counter(token.text.lower() for token in doc if token.is_alpha)

for word, count in word_count.items():
    print(f"Word: '{word}' - Count: {count}")