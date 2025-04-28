from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        days = int(request.form["days"])
        slots = int(request.form["slots"])
        subjects = request.form["subjects"].split(",")

        timetable = []
        for _ in range(slots):
            timetable.append([random.choice(subjects) for _ in range(days)])

        return render_template("timetable.html", days=days, slots=slots, timetable=timetable)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
