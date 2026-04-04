#!/usr/bin/python3
"""Module for Flask app displaying data from JSON or CSV."""
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)


@app.route("/")
def home():
    """Render the home page."""
    return render_template("index.html")


@app.route("/about")
def about():
    """Render the about page."""
    return render_template("about.html")


@app.route("/contact")
def contact():
    """Render the contact page."""
    return render_template("contact.html")


@app.route("/items")
def items():
    """Render items from JSON file."""
    try:
        with open("items.json", "r") as f:
            data = json.load(f)
        item_list = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        item_list = []
    return render_template("items.html", items=item_list)


@app.route("/products")
def products():
    """Render products from JSON or CSV based on query parameter."""
    source = request.args.get("source")
    error = None
    product_list = []

    if source == "json":
        try:
            with open("products.json", "r") as f:
                product_list = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            error = "Error reading JSON file."
    elif source == "csv":
        try:
            with open("products.csv", "r") as f:
                reader = csv.DictReader(f)
                product_list = [row for row in reader]
        except FileNotFoundError:
            error = "Error reading CSV file."
    else:
        error = "Wrong source. Please use 'json' or 'csv'."

    return render_template(
        "product_display.html", products=product_list, error=error
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
