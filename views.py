from flask import Flask, render_template, request, url_for
from utils import get_available_curr, rate_engine
import requests
import os

app = Flask(__name__)

# Adding a secret API_V6_KEY from .env
API_KEY = os.getenv("API_KEY")

# Show main kantor page
@app.route("/", methods=["GET", "POST"])
def get_start():
    return render_template("page.html", ctx={"from_curr_name": get_available_curr()})


@app.route("/calculation", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return rate_engine(
            amount=float(request.args.get("amount")),
            from_curr=request.args.get("from_curr"),
            to_curr=request.args.get("to_curr")
        )
