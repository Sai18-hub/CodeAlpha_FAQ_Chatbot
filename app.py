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
@app.route("/api")
@app.route("/api/index")
@app.route("/api/index.py")
def home():
    try:
        return render_template("index.html")
    except Exception:
        index_path = os.path.join(base_dir, "index.html")
        if os.path.exists(index_path):
            with open(index_path, "r", encoding="utf-8") as f:
                return f.read(), 200, {"Content-Type": "text/html"}
        return "AI FAQ Chatbot is running", 200


@app.route("/chat", methods=["POST"])
@app.route("/api/chat", methods=["POST"])
@app.route("/api/index/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
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


@app.route("/<path:path>", methods=["GET", "POST"])
def catch_all(path):
    if request.method == "POST":
        return chat()
    return home()


if __name__ == "__main__":
    app.run(debug=True)