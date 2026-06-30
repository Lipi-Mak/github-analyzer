from flask import Flask, render_template, request
from analyzer import analyze_profile
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def home():
    report = None
    if request.method == "POST":
        username = request.form.get("username")
        report = analyze_profile(username)
    return render_template("index.html", report=report)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)