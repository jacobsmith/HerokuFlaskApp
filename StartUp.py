
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')

def index():

	return render_template("Main.html")

if __name__ == "__main__":
	app.run()
