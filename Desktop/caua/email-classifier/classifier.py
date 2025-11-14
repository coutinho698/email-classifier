import pickle

# Carregar modelo e vetorizador
with open("model.pkl", "rb") as f:
    data = pickle.load(f)

# Compatível com os dois formatos:
# - antigo: (model, vectorizer)
# - novo: {"model": model, "vectorizer": vectorizer}
if isinstance(data, dict):
    model = data["model"]
    vectorizer = data["vectorizer"]
else:
    # supõe que seja uma tupla (model, vectorizer)
    model, vectorizer = data

def classify_email(text: str) -> str:
    """Recebe o texto do e-mail e retorna a classe prevista."""
    vector = vectorizer.transform([text])
    prediction = model.predict(vector)[0]
    return prediction
