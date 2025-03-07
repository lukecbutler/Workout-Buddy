from flask import Flask, render_template, redirect, request
import sqlite3

# Initilize Flask App
app = Flask(__name__)

DATABASE = "workouts.db"

def getDbConnection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection

@app.route("/")
def home():
    return render_template("homepage.html")

# Main function
if __name__ == "__main__":
    app.run(debug=True)