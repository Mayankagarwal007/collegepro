import requests
import time
from datetime import datetime, timedelta
from flask import Flask, render_template, request


app = Flask("Attendance")

@app.route("/")
def home():
    return render_template("index.html")


app.run(debug=True)