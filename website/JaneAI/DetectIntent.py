# import re
import json
import os

PRODUCTION = True

if PRODUCTION == True:
    data_location_prefix = "futo-space-database"
else:
    data_location_prefix = ""

file_path = os.path.join(data_location_prefix, "website", "JaneAI", "Training Data", "predefined_intents.json")

with open(data_location_prefix + file_path, "r") as intent_dict_file:
    INTENTS: dict = json.load(intent_dict_file)

def detect_intent(user_input: str):
    version = "1.0.0"
    if version != "1.0.0":
        # Lemmatize user input
        lemmatized_input = user_input# lemmatize_sentence(user_input)

        # Iterate through intents and keywords
        for intent, keywords in INTENTS.items():
            # Lemmatize keywords for comparison
            lemmatized_keywords = []# [lemmatizer.lemmatize(keyword.lower()) for keyword in keywords]
        
            # Check if any keyword matches the lemmatized user input
            if any(keyword in lemmatized_input for keyword in lemmatized_keywords):
                return intent

        return "unknown_intent"
    
    user_input = user_input.lower()

    for intent, keywords in INTENTS.items():
        if any(keyword in user_input for keyword in keywords):
            return intent

    return "unknown_intent"

# # Detect intent based on lemmatized words and synonyms
# def detect_intent(user_input):
#     
