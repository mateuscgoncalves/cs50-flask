from flask import Flask, render_template, request, redirect

app = Flask(__name__)

SPORTS = [
    "basketball",
    "soccer",
    "frisbee"
]

REGISTRANTS = {}

@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():

    name = request.form.get("name")
    if not name:
        return render_template("failure.html", message="Missing name")

    sport = request.form.get("sport")
    if not sport:
        return render_template("failure.html", message="Missing sport")

    if sport not in SPORTS:
        return render_template("failure.html")

    REGISTRANTS[name] = sport
    return redirect("/registrants")


@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=REGISTRANTS)
