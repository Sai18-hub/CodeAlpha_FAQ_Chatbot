import os
import json
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load FAQ data
_current_dir = os.path.dirname(os.path.abspath(__file__))
_faq_path = os.path.join(_current_dir, "faqs.json")
with open(_faq_path, "r", encoding="utf-8") as file:
    faqs = json.load(file)


# Text preprocessing function
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


# Prepare FAQ questions
questions = [
    preprocess_text(faq["question"])
    for faq in faqs
]


# Convert questions into TF-IDF vectors
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)


# Find the best answer
def get_response(user_question):

    user_question = preprocess_text(user_question)

    # Convert user question into TF-IDF vector
    user_vector = vectorizer.transform([user_question])

    # Calculate cosine similarity
    similarity_scores = cosine_similarity(
        user_vector,
        question_vectors
    )[0]

    # Find highest similarity
    best_match_index = similarity_scores.argmax()
    best_score = similarity_scores[best_match_index]

    # Minimum confidence threshold
    if best_score < 0.25:
        return (
            "Sorry, I don't have an answer for that question.",
            best_score
        )

    answer = faqs[best_match_index]["answer"]

    return answer, best_score


# Test chatbot
if __name__ == "__main__":

    print("=================================")
    print("      AI FAQ CHATBOT")
    print("=================================")
    print("Type 'exit' to stop the chatbot.\n")

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Bot: Thank you! Goodbye.")
            break

        response, score = get_response(user_input)

        print(f"Bot: {response}")
        print(f"Similarity: {score:.2f}\n")