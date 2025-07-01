from flask import Flask, render_template, request
from gtts import gTTS
import os

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
        if texto.strip():
            tts = gTTS(text=texto, lang='es', tld='com.mx')  # voz femenina
            tts.save("static/voz.mp3")
    return render_template("index.html", texto=texto, frases=frases_por_defecto)

if __name__ == "__main__":
    app.run(debug=True)
