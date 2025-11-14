import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

print("🔄 Iniciando treinamento do modelo...")

# Dataset simples já embutido
data = {
    "email": [
        "Preciso de atualização sobre o status da minha solicitação.",
        "Segue o arquivo para análise.",
        "Feliz Natal para toda a equipe!",
        "Obrigado pelo excelente trabalho.",
        "Pode verificar o erro no sistema?",
        "Bom dia! Apenas passando para agradecer."
    ],
    "label": ["produtivo", "produtivo", "improdutivo", "improdutivo", "produtivo", "improdutivo"]
}

df = pd.DataFrame(data)

print("📊 Dataset carregado!")

# Vetorização
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["email"])
y = df["label"]

print("🔤 Texto transformado em vetores!")

# Treino com regressão logística
model = LogisticRegression()
model.fit(X, y)

print("🤖 Modelo treinado com sucesso!")

# Salvando o modelo
with open("model.pkl", "wb") as f:
    pickle.dump({"model": model, "vectorizer": vectorizer}, f)

print("💾 Modelo salvo como model.pkl!")
print("🎯 Treinamento finalizado!")
