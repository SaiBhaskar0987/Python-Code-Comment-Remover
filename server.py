from flask import Flask, request, send_file, render_template
import subprocess
import os

app = Flask(__name__)

# Temporary folder to store uploaded and processed files
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

@app.route("/", methods=["GET"])
def index():
    return render_template("seen.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No file uploaded", 400

    file = request.files["file"]
    if file.filename == "":
        return "No file selected", 400

    if not file.filename.endswith(".py"):
        return "Only .py files are allowed", 400

    upload_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(upload_path)

    output_path = os.path.join(OUTPUT_FOLDER, "output_" + file.filename)
    try:
        subprocess.run(["python", "main.py", upload_path, output_path], check=True)
    except subprocess.CalledProcessError as e:
        return f"Error processing file: {e}", 500

    # Return the processed file for download
    return send_file(output_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)