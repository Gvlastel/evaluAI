from flask import Flask, render_template, request, redirect, url_for, session, send_file
from auth import check_user
from file_processing import process_uploaded_files
from comparison import compare_quotes, generate_excel

import os

app = Flask(__name__)
app.secret_key = "YOUR_SECRET_KEY"  # Reemplaza por una clave segura

@app.route("/")
def index():
    return render_template("welcome.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        password = request.form["password"]
        if check_user(user, password):
            session["user"] = user
            return redirect(url_for("upload"))
        else:
            return render_template("login.html", error="Credenciales inválidas")
    return render_template("login.html")

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if "user" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        files = request.files.getlist("files")
        file_paths = process_uploaded_files(files)
        session["files"] = file_paths
        return redirect(url_for("compare"))
    return render_template("upload.html")

@app.route("/compare")
def compare():
    if "files" not in session:
        return redirect(url_for("upload"))
    results, summary = compare_quotes(session["files"])
    generate_excel(results, summary)
    return render_template("comparison.html", results=results, summary=summary)

@app.route("/download")
def download():
    return send_file("output/comparison_results.xlsx", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
