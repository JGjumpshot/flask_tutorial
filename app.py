from flask import Flask, render_template, request
import smtplib
from dotenv import load_dotenv
import os
load_dotenv()
app = Flask(__name__)

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

@app.route("/")
def index():
    title = "Jackson Gunther's Portfolio"
    return render_template("index.html", title=title)

@app.route("/about")
def about():
    names = ["Melanie", "Kris", "Sandy", "Tucker"]
    return render_template("about.html", names=names)

@app.route("/subscribe")
def subscribe():
    return render_template("subscribe.html")

@app.route("/form", methods=["POST"])
def form():
    first_name = request.form.get("first_name")
    last_name = request.form.get("last_name")
    email = request.form.get("email")

    message = "You have been subscribed to my email newsletter"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL, PASSWORD)
    server.sendmail(EMAIL, email, message)

    if not first_name or not last_name or not email:
        error_statement = "All form fields required"
        return render_template("subscribe.html", error_statement= error_statement,
        first_name=first_name,
        last_name=last_name,
        email=email
        )
    return render_template("form.html", first_name=first_name, last_name=last_name, email=email)