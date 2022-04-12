# pylint: disable=missing-function-docstring
from flask import Flask, render_template, request, url_for, redirect
import csv

app = Flask(__name__)


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


@app.route("/")
@app.route("/index")
@app.route("/index.html")
def home():
    return render_template("index.html")


@app.route("/<username>/<int:post_id>")
def users_posts(username=None, post_id=None):
    return render_template("/posts.html", username=username, post_id=post_id)


def write_to_db(data):
    with open("database.txt", mode="a", encoding="utf-8") as db:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        # file =
        db.write(f"\n{email},{subject}, {message}")


def write_to_csv(data):
    with open("database.csv", mode="a", encoding="utf-8", newline="") as db2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]

        csv_writer = csv.writer(db2, quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("thanks.html")
        except:
            return "Did not save to DB"
    return "Form submitted not submitted Onidodo!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003,debug=True)
