from flask import Flask, render_template, redirect, request
from flask_login import 
import sqlite3

# Initilize Flask App
app = Flask(__name__)

DATABASE = "workouts.db"

@app.route("/")
def home():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    return render_template("homepage.html")

# Main function
if __name__ == "__main__":
    app.run(debug=True, port=80, host='0.0.0.0')