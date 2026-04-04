#!/usr/bin/python3
"""Module for Flask app with SQLite integration."""
from flask import Flask, render_template, request
import json
import csv
import sqlite3

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
    """Render products from JSON, CSV, or SQL based on query parameter."""
    source = request.args.get("source")
    product_id = request.args.get("id")
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
    elif source == "sql":
        try:
            conn = sqlite3.connect("products.db")
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            if product_id:
                cursor.execute(
                    "SELECT id, name, category, price FROM Products WHERE id = ?",
                    (product_id,)
                )
            else:
                cursor.execute(
                    "SELECT id, name, category, price FROM Products"
                )
            rows = cursor.fetchall()
            product_list = [
                {"id": r["id"], "name": r["name"],
                 "category": r["category"], "price": r["price"]}
                for r in rows
            ]
            conn.close()
            if product_id and not product_list:
                error = "Product not found"
        except sqlite3.Error:
            error = "Error reading SQLite database."
    else:
        error = "Wrong source"

    if not error and product_id and source != "sql":
        filtered = [
            p for p in product_list
            if str(p.get("id", "")) == str(product_id)
        ]
        if not filtered:
            error = "Product not found"
            product_list = []
        else:
            product_list = filtered

    return render_template(
        "product_display.html", products=product_list, error=error
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
