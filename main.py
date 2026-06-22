from transformers import pipeline
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
classifier = pipeline("sentiment-analysis") # type: ignore

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data["text"]

    result = classifier(text)[0]

    return jsonify({
        "label": result["label"],
        "score": float(result["score"])
    })
if __name__ == "__main__":
    app.run(debug=True)