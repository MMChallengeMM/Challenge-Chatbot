from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np

app = Flask(__name__)
CORS(app)

model = pd.read_pickle("../models/modelo_treinado.pkl")

@app.route("/prever", methods=["POST"])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])
    df_encoded = pd.get_dummies(df)
    
    colunas_modelo = model.feature_names_in_
    for col in colunas_modelo:
        if col not in df_encoded.columns:
            df_encoded[col] = 0
    df_encoded = df_encoded[colunas_modelo]

    pred = model.predict(df_encoded)[0]
    return jsonify({'interrupcao_prevista_h': round(pred, 2)})

if __name__ == '__main__':
    app.run(debug=True)