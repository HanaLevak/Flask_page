import os
import json
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/stuff")
def about():
    items = []
    with open("data/reagents.json", "r") as json_data:
        items = json.load(json_data)
    return render_template("stuff.html", page_title="Stuff", reagents=items)


@app.route("/misc")
def item_name():
    item_name = {}
    with open("data/reagents.json", "r") as json_data:
        item_name = json.load(json_data)
    return render_template("misc.html", page_title="Misc", items=item_name)


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)
