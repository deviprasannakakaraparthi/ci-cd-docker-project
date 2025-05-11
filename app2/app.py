from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Application 2 - UPDATED!"
