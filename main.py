from flask import Flask, render_template
import os
import jinja2

app = Flask(__name__)

@app.route('/')
def home():
  return render_template("home.html")

@app.route('/python')
def python():
  return render_template("python.html")

@app.route('/HTML')
def HTML():
  return render_template("HTML.html")

if __name__ == "__main.py__":
  app.run(debug=True, port='5000', host='127.0.0.1')