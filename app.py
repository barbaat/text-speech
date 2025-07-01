from flask import Flask, render_template, request, send_from_directory, url_for
from gtts import gTTS
import os
import uuid

app = Flask(__name__)

AUDIO_DIR = "static/audios"
os.makedirs(AUDIO_DIR, exist_ok=True)

frases_por_defecto = [
    "Hola, ¿cómo estás?",
    "Bienvenido a nuestra aplicación.",
    "Gracias por usar este servicio."
]

@app.route("/", methods=["GET", "POST"])
def index():
    texto = ""
    audio_filename = ""
    if request.method == "POST":
        texto = request.form["texto"]
        if texto.strip():
            audio_filename = f"{uuid.uuid4()}.mp3"
            path = os.path.join(AUDIO_DIR, audio_filename)
            tts = gTTS(text=texto, lang='es', tld='com.mx')
            tts.save(path)
    return render_template("index.html", texto=texto, audio_filename=audio_filename, frases=frases_por_defecto)

@app.route("/audio/<filename>")
def audio(filename):
    return send_from_directory(AUDIO_DIR, filename)

if __name__ == "__main__":
    app.run(debug=True)
