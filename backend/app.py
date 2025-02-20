from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
from backend.models.transcriber import transcribe_video
from backend.models.analyzer import analyze_text

app = Flask(__name__)
CORS(app)  # Gérer les requêtes cross-origin

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_video():
    if "file" not in request.files:
        return jsonify({"error": "Aucun fichier reçu"}), 400
    file = request.files["file"]
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(filepath)

    transcription = transcribe_video(filepath)
    analysis = analyze_text(transcription)

    return jsonify({"transcription": transcription, "analysis": analysis})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Utilise le port donné par Render
    app.run(host="0.0.0.0", port=port)
