import spacy
from collections import defaultdict

nlp = spacy.load("en_core_web_sm")

def summarize_text(text, num_sentences=2):
    doc = nlp(text)

    sentence_scores = defaultdict(int)
    for sent in doc.sents:
        for token in sent:
            if not token.is_stop and not token.is_punct:
                sentence_scores[sent] += token.rank

    summarized_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    
    return ' '.join([str(sent) for sent in summarized_sentences])

article = """Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga, kas ir slavena ar savu vēsturisko centru un skaistajām ēkām. Latvija robežojas ar Lietuvu, Igauniju un Krieviju, kā arī tai ir piekļuve Baltijas jūrai. Tā ir viena no Eiropas Savienības dalībvalstīm."""

summary = summarize_text(article)
print(f"Summary: {summary}")
