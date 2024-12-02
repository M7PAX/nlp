import spacy

def extract_keywords(text):
    """
    Extracts key words from the given text using SpaCy.
    Focuses on nouns, proper nouns, and verbs.
    """
    # Load SpaCy's English model
    nlp = spacy.load("en_core_web_sm")
    
    # Process the text
    doc = nlp(text)
    
    # Define parts of speech to consider as keywords
    keywords = [token.text for token in doc if token.pos_ in {"NOUN", "PROPN", "VERB"}]
    
    return keywords

# Example usage
if __name__ == "__main__":
    user_input = input("Enter a question or command: ")
    keywords = extract_keywords(user_input)
    print("Extracted Keywords:", keywords)