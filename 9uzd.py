from transformers import pipeline
from translate import Translator

text = "Reiz kādā tālā zemē..."

text_generator = pipeline("text-generation", model="gpt2")

text = Translator(from_lang="lv", to_lang="en").translate(text)
json = text_generator(
    text,
    max_length=70,
    num_return_sequences=1,
    temperature=1.2,
    truncation=True
)

print(Translator(from_lang="en", to_lang="lv").translate(json[0]["generated_text"])) 
