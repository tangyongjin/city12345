import os
import tempfile
from audio_processing import transcribe_audio, ask_gpt
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai

openai.api_key = os.environ.get("OPENAI_API_KEY")

app = Flask(__name__, static_folder="static", static_url_path="/")

UPLOAD_FOLDER = "/ruta/donde/deseas/guardar/los/archivos"
ALLOWED_EXTENSIONS = {"wav"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["TEMPLATES_AUTO_RELOAD"] = True
CORS(app)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/transcribe", methods=["POST"])
def transcribe():
    audio_file = request.files.get("audio")
    if audio_file is not None:
        # Crea un archivo temporal para guardar el audio recibido
        with tempfile.NamedTemporaryFile(delete=False, suffix=".webm") as temp:
            audio_file.save(temp.name)
            print("- 💟💟💟💟💟💟💟💟💟💟💟💟💟💟💟💟💟 -")
            print(temp.name)
            temp.flush()

            # 调用GPT-3
            # Transcribe el archivo de audio
            transcription = transcribe_audio(temp.name)

            os.unlink(temp.name)

            print("- 💟💟💟💟💟💟💟💟💟💟💟💟💟💟💟💟💟 -")
            print(transcription)
            question = transcription.text
            print("-     🌼🌼🌼🌼🌼 捕捉到文本 >>>>>>>> ")
            print(question)
            print("-     <<<<<<< 捕捉到文本 🌼🌼🌼🌼 ")

            # # 调用GPT-3
            # # Transcribe el archivo de audio
            # transcription = "我家附近老有摩托车,很吵,晚上尤其严重"
            # # Elimina el archivo temporal
            # os.unlink(temp.name)
            # # Consulta a GPT con la transcripción
            # answer = "生态环境保
            summary_obj = ask_gpt(question)

            print(" summary_obj >>>>>>>>>: 🌺🌺🌺🌺🌺🌺🌺🌺🌺🌺🌺🌺🌺🌺🌺 ")
            print(summary_obj)
            print("        🌺🌺🌺🌺🌺🌺🌺🌺🌺🌺🌺🌺🌺🌺🌺 <<<<<<<  ")

            answer = summary_obj.choices[0].text.strip()
            return jsonify({"transcription": question, "answer": answer})

    return jsonify({"error": "No audio file received"})


if __name__ == "__main__":
    app.run(debug=True)
