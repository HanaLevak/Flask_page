import os
import json
from flask import Flask, render_template, request, flash


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html",  page_title="Home")


@app.route("/legends")
def legends():
    item = []
    with open("data/legends.json", "r")as json_data:
        data =json.load(json_data)
    return render_template("legends.html", page_title="Legends")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash("Thanks {}, we have received your message!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
