from flask import Flask, render_template, request, send_file
from gtts import gTTS
from io import BytesIO

app = Flask(__name__)

frases_por_defecto = [
    "Hola, ¿cómo estás?",
    "Bienvenido a nuestra aplicación.",
    "Gracias por usar este servicio."
]

@app.route("/", methods=["GET", "POST"])
def index():
    texto = ""
    if request.method == "POST":
        texto = request.form["texto"]
    return render_template("index.html", texto=texto, frases=frases_por_defecto)

@app.route("/audio", methods=["POST"])
def audio():
    texto = request.form.get("texto", "")
    if not texto.strip():
        return "", 204
    tts = gTTS(text=texto, lang='es', tld='com.mx')
    mp3_fp = BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    return send_file(mp3_fp, mimetype="audio/mpeg")

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Render usa una variable PORT
    app.run(host="0.0.0.0", port=port)

