from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
import os

app = Flask(__name__)

MONGO_URI = "mongodb+srv://prasannastrato_db_user:lexlHCzfn9EE1zPm@cluster0.5glz12y.mongodb.net/kpdb?retryWrites=true&w=majority" #os.environ.get("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client["mydatabase"]
collection = db["users"]

@app.route('/')
def form():
    return render_template("form.html")

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form.get("name")
        email = request.form.get("email")

        if not name or not email:
            return render_template("form.html", error="All fields are required")

        collection.insert_one({
            "name": name,
            "email": email
        })

        return redirect(url_for("success"))

    except Exception as e:
        return render_template("form.html", error=str(e))

@app.route('/success')
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
