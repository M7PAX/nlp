import spacy
from sklearn.metrics.pairwise import cosine_similarity
from deep_translator import GoogleTranslator

words_lv = ["māja", "dzīvoklis", "jūra"]

def translate_words(words):
    translations = []
    for word in words:
        translated_word = GoogleTranslator(source='lv', target='en').translate(word)
        translations.append(translated_word)
    return translations

words_en = translate_words(words_lv)

nlp = spacy.load("en_core_web_md")

def get_embeddings(words):
    embeddings = []
    for word in words:
        doc = nlp(word)
        embeddings.append(doc.vector)
    return embeddings

embeddings = get_embeddings(words_en)

similarities = cosine_similarity(embeddings)

for i in range(len(words_en)):
    for j in range(i + 1, len(words_en)):
        print(f"Similarity between '{words_en[i]}' and '{words_en[j]}': {similarities[i][j]:.4f}")
