from flask import Flask, render_template, request
from utils import get_available_curr, validate_form
from exchange import exchange_engine

app = Flask(__name__)

# Show main kantor page
@app.route("/")
def get_start():
    return render_template("page.html", ctx={"available_curr": get_available_curr()})

# Create calculate layer
@app.route("/calculate", methods=["POST"])
def calculate():
    curr_to_sell = request.form["curr_to_sell"]
    curr_to_buy = request.form["curr_to_buy"]
    amount = request.form["amount"]
    errors = validate_form(curr_to_sell, curr_to_buy, amount)
    if errors == []:
        res = exchange_engine(
            curr_to_sell=curr_to_sell, curr_to_buy=curr_to_buy, amount=amount
        )
        return str(res)
    else:
        return render_template(
            "page.html",
            ctx={
                "errors": errors,
                "curr_to_sell": curr_to_sell,
                "curr_to_buy": curr_to_buy,
                "amount": amount,
                "available_curr": get_available_curr(),
            },
        )
# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500