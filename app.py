from ai import chatbot_response, detect_fake_news, analyze_complaint
from flask import Flask, render_template, request, redirect, session

from database import create_database, add_user, get_user

from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.secret_key="civicpulse_secret_key"

# Initialize Database
create_database()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET","POST"])
def login():

    if request.method=="POST":

        email=request.form["email"]

        password=request.form["password"]


        user=get_user(email)


        if user and check_password_hash(user[3],password):

            session["user"]=user[1]

            return redirect("/dashboard")


    return render_template("login.html")


@app.route("/register", methods=["GET","POST"])
def register():

    if request.method=="POST":

        username=request.form["username"]

        email=request.form["email"]

        password=request.form["password"]


        hashed_password = generate_password_hash(password)


        add_user(
            username,
            email,
            hashed_password
        )


        return redirect("/login")


    return render_template("register.html")

@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect("/login")

    return render_template("dashboard.html")

@app.route("/chatbot", methods=["GET", "POST"])
def chatbot():

    if "user" not in session:
        return redirect("/login")

    if request.method == "POST":

        question = request.form["question"]

        answer = chatbot_response(question)

        return render_template(
            "chatbot.html",
            question=question,
            answer=answer
        )

    return render_template("chatbot.html")

@app.route("/crowd", methods=["GET","POST"])
def crowd():

    result=None

    if request.method=="POST":

        result="Crowd Level: Medium\nPeople Count: Approx 150\nRisk: Low"

    return render_template(
        "crowd.html",
        result=result
    )

@app.route("/fake-news", methods=["GET", "POST"])
def fake_news():

    if "user" not in session:
        return redirect("/login")

    result = None

    if request.method == "POST":

        news = request.form["news"]

        result = detect_fake_news(news)

    return render_template(
        "fake_news.html",
        result=result
    )
@app.route("/complaints", methods=["GET","POST"])
def complaints():

    if "user" not in session:
        return redirect("/login")

    result=None

    if request.method=="POST":

        text=request.form["complaint"]

        result=analyze_complaint(text)

    return render_template(
        "complaints.html",
        result=result
    )

@app.route("/report")
def report():

    if "user" not in session:
        return redirect("/login")

    data="""
CivicPulse AI Report

Crowd Status: Medium

Fake News Cases: 3

Complaints: 12

AI Status: Active
"""

    return render_template(
        "report.html",
        report=data
    )
@app.route("/admin")
def admin():
    
    if "user" not in session:
        return redirect("/login")
    return render_template("admin.html")


@app.route("/profile")
def profile():
    if "user" not in session:
        return redirect("/login")
    return render_template("profile.html")

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000)