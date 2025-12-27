from flask import Flask, render_template, request
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    name = request.form.get("name", "")
    phone = request.form.get("phone", "")
    address = request.form.get("address", "")
    message = request.form.get("message", "")
    
    # Save to file with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("inquiries.txt", "a", encoding="utf-8") as f:
        f.write(f"{timestamp} | {name} | {phone} | {address} | {message}\n")
    
    return "OK"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
