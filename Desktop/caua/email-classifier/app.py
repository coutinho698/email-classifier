from flask import Flask, render_template, request
from classifier import classify_email
from response_generator import generate_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    auto_reply = None

    if request.method == "POST":
        text = request.form.get("email_text", "").strip()

        if text:
            label = classify_email(text)
            result = f"Categoria detectada: {label}"
            auto_reply = generate_response(label)
        else:
            result = "Nenhum texto informado."
            auto_reply = None

    return render_template("index.html", result=result, auto_reply=auto_reply)


if __name__ == "__main__":
    print("🚀 Iniciando aplicação Flask em http://127.0.0.1:5000 ...")
    app.run(debug=True)
