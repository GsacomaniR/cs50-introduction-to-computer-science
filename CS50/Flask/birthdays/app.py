import os
from cs50 import SQL
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Configure SQLite database
db = SQL("sqlite:///birthdays.db")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get form data
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")

        # Validate input (optional but recommended)
        if name and month and day:
            # Insert new birthday into database
            db.execute("INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)",
                      name, month, day)

        # Redirect back to GET request
        return redirect("/")

    else:
        # Query database for all birthdays
        birthdays = db.execute("SELECT * FROM birthdays ORDER BY month, day")

        # Render index.html with birthdays data
        return render_template("index.html", birthdays=birthdays)

# Optional: Add route for deleting birthdays
@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    db.execute("DELETE FROM birthdays WHERE id = ?", id)
    return redirect("/")

# Optional: Add route for editing birthdays
@app.route("/edit/<int:id>", methods=["POST"])
def edit(id):
    name = request.form.get("name")
    month = request.form.get("month")
    day = request.form.get("day")

    if name and month and day:
        db.execute("UPDATE birthdays SET name = ?, month = ?, day = ? WHERE id = ?",
                  name, month, day, id)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
