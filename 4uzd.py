from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("DGurgurov/xlm-r_latvian_sentiment")
model = AutoModelForSequenceClassification.from_pretrained("DGurgurov/xlm-r_latvian_sentiment")

sentences = [
    "Šis produkts ir lielisks, esmu ļoti apmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts, nekas īpašs."
]

inputs = tokenizer(sentences, padding=True, truncation=True, return_tensors="pt")

with torch.no_grad():
    outputs = model(**inputs)

predictions = torch.argmax(outputs.logits, dim=-1)

labels = ["Negative", "Neutral", "Positive"]

for sentence, prediction in zip(sentences, predictions):
    print(f"'{sentence}' - {labels[prediction]}")
