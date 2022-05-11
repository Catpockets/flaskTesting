from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "P0s31d0n"

@app.route("/hello")
def index():
	flash("What's your name Playa?")
	return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greeter():
    flash("Sup " + str(request.form['name_input']) + ", nice meetin' ya")
    request.form['name_input']
    return render_template("index.html")