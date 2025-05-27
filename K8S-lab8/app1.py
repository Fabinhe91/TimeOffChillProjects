from flask import Flask, request, jsonify
from flask_cors import CORS  # Importando o CORS

app = Flask(__name__)

# Habilitar CORS para todas as rotas
CORS(app)

wines = []

@app.route('/wines', methods=['GET'])
def get_wines():
    return jsonify(wines)

@app.route('/wines', methods=['POST'])
def add_wine():
    new_wine = request.get_json()
    wines.append(new_wine)
    return jsonify(new_wine), 201

if __name__ == "__main__":
    app.run(debug=True)
