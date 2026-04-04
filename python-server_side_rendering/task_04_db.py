#!/usr/bin/python3
"""Module for Flask app with SQLite integration."""
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)


def create_database():
    """Create SQLite database and populate with sample data."""
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS Products ("
        "id INTEGER PRIMARY KEY, "
        "name TEXT NOT NULL, "
        "category TEXT NOT NULL, "
        "price REAL NOT NULL)"
    )
    cursor.execute("DELETE FROM Products")
    cursor.execute(
        "INSERT INTO Products VALUES (1, 'Laptop', 'Electronics', 799.99)"
    )
    cursor.execute(
        "INSERT INTO Products VALUES (2, 'Coffee Mug', 'Kitchen', 15.99)"
    )
    cursor.execute(
        "INSERT INTO Products VALUES (3, 'Desk Chair', 'Furniture', 249.99)"
    )
    conn.commit()
    conn.close()


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
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, category, price FROM Products")
            rows = cursor.fetchall()
            product_list = [
                {"id": r[0], "name": r[1], "category": r[2], "price": r[3]}
                for r in rows
            ]
            conn.close()
        except sqlite3.Error:
            error = "Error reading SQLite database."
    else:
        error = "Wrong source. Please use 'json', 'csv', or 'sql'."

    return render_template(
        "product_display.html", products=product_list, error=error
    )


if __name__ == "__main__":
    create_database()
    app.run(debug=True, port=5000)
