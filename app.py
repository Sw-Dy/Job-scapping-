from flask import Flask, render_template, request
from scraper import fetch_jobs

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    jobs = []
    if request.method == "POST":
        role = request.form.get("role")
        location = request.form.get("location")
        experience = request.form.get("experience")
        
        jobs = fetch_jobs(role, location, experience)

    return render_template("index.html", jobs=jobs)

if __name__ == "__main__":
    app.run(debug=True,port=5009)
