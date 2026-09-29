# CodeAlpha FAQ Chatbot

An AI-based FAQ Chatbot developed as part of the CodeAlpha Artificial Intelligence Internship.

The chatbot uses Natural Language Processing (NLP), TF-IDF vectorization, and Cosine Similarity to understand user questions and provide the most relevant answer from a predefined FAQ dataset.

## Features

- AI-based FAQ question matching
- Natural Language Processing
- Text preprocessing
- TF-IDF vectorization
- Cosine Similarity
- Similarity threshold for unknown questions
- Flask web application
- Interactive chat interface
- Responsive and simple UI
- Predefined FAQ dataset
- Real-time responses

## Technologies Used

- Python
- Flask
- Scikit-learn
- NLTK
- HTML
- CSS
- JavaScript
- TF-IDF
- Cosine Similarity

## How It Works

The chatbot follows these steps:

1. The user enters a question.
2. The question is converted to lowercase and cleaned.
3. The FAQ questions are converted into TF-IDF vectors.
4. The user's question is also converted into a TF-IDF vector.
5. Cosine Similarity is calculated between the user's question and all FAQ questions.
6. The FAQ with the highest similarity score is selected.
7. The corresponding answer is returned to the user.
8. If the similarity score is below the threshold, the chatbot informs the user that it does not have an answer.

## Project Structure

```text
CodeAlpha_FAQ_Chatbot/
│
├── app.py
├── chatbot.py
├── faqs.json
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│   └── index.html
│
└── static/
    ├── style.css
    └── script.js