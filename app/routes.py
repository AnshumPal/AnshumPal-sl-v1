# from app import app

# @app.route("/")
# def home():
#     return "Welcome to My Flask App!"
from app import app 
from flask import render_template


# @app.route("/")
# def home():
#     return render_template("index.html")


@app.route("/Anshum")
def home():
    return render_template("portfolio.html")

