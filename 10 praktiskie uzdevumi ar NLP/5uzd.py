import re

raw_text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"

def clean_text(text):
    text = re.sub(r'@\w+:?', '', text)
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'[!?:]+', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    text = text.lower()
    return text

cleaned_text = clean_text(raw_text)

print(cleaned_text)
