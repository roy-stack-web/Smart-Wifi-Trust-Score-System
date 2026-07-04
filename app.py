from flask import Flask, render_template
from scanner import scan_network

app = Flask(__name__)


@app.route("/")
def home():
    devices = scan_network("192.168.9.0/24")
    return render_template("index.html", devices=devices)


if __name__ == "__main__":
    app.run(debug=True)