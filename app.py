from flask import Flask, render_template, request
from database import data

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search")
def search():
    query = request.args.get("q").lower()
    hasil_pencarian = []

    for item in data:
        if query in item["keyword"]:
            hasil_pencarian.append(item["hasil"])

    return render_template("result.html", query=query, results=hasil_pencarian)

from flask import jsonify

@app.route("/suggest")
def suggest():

    query = request.args.get("q","").lower()
    suggestions = []

    for item in data:
        if query in item["keyword"]:
            suggestions.append(item["keyword"])

    return jsonify(suggestions)

if __name__ == "__main__":
    app.run(debug=True)