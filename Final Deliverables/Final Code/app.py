from markupsafe import escape
from flask import Flask, render_template, url_for, redirect,request
from flask_mail import Mail,Message


app = Flask(__name__,template_folder="templates")


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login.html")
def login():
    return render_template("login.html")

@app.route("/contactus.html")
def contactus():
    return render_template("contactus.html")
def back():
     return ("home.html")
 
@app.route("/men.html")
def men():
    return render_template("men.html")

@app.route("/women.html")
def women():
    return render_template("women.html")
 
@app.route("/tracking.html")
def tracking():
    return render_template("tracking.html")

@app.route("/shopnow.html")
def shopnow():
    return render_template("shopnow.html")

@app.route("/confirmation.html")
def confirmation():
    return render_template("confirmation.html")
    return ("home.html")

@app.route("/kid.html")
def kid():
    return render_template("kid.html")

if __name__ == "__main__":
    app.run(debug=True)