import pickle

# Carregar modelo
with open("model.pkl", "rb") as f:
    data = pickle.load(f)

model = data["model"]
vectorizer = data["vectorizer"]

def classify_email(text):
    if not text:
        return None
    vector = vectorizer.transform([text])
    prediction = model.predict(vector)[0]
    return prediction
