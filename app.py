import os
from flask import Flask, render_template, request, jsonify
from chatbot import get_response

base_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(base_dir, "templates"),
    static_folder=os.path.join(base_dir, "static")
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()
    user_message = data.get("message", "")

    if not user_message.strip():
        return jsonify({
            "response": "Please enter a question."
        })

    response, score = get_response(user_message)

    return jsonify({
        "response": response,
        "similarity": round(score, 2)
    })


if __name__ == "__main__":
    app.run(debug=True)