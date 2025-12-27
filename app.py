from flask import Flask, render_template, request
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/admin")
def admin():
    inquiries = []
    try:
        if os.path.exists("inquiries.txt"):
            with open("inquiries.txt", "r", encoding="utf-8") as f:
                inquiries = [line.strip() for line in f.readlines() if line.strip()]
        if not inquiries:
            inquiries = ["No inquiries yet"]
    except:
        inquiries = ["No inquiries yet"]
    return render_template("admin.html", inquiries=inquiries)

@app.route("/contact", methods=["POST"])
def contact():
    try:
        name = request.form.get("name", "")
        phone = request.form.get("phone", "")
        address = request.form.get("address", "")
        message = request.form.get("message", "")
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("inquiries.txt", "a", encoding="utf-8") as f:
            f.write(f"{timestamp} | {name} | {phone} | {address} | {message}\n")
        return "OK"
    except:
        return "Error"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
