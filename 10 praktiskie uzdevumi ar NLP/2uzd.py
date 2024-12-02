from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0

texts = [
    "Šodien ir saulaina diena.",
    "Today is a sunny day.",
    "Сегодня солнечный день."
]

def detect_language(text):
    try:
        return detect(text)
    except Exception as e:
        return str(e)

for text in texts:
    language = detect_language(text)
    print(f"Text: '{text}' - Detected Language: {language}")
