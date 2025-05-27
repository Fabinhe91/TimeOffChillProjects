from flask import Flask, request, jsonify
from flask_cors import CORS

# Habilitar CORS para todas as rotas
CORS(app, resources={r"/wines/*": {"origins": "http://localhost:8000"}})


# Dados de exemplo
wines = []

app = Flask(__name__)

# Configuração do banco de dados
db_config = {
    'host': 'db',  # Nome do serviço Kubernetes para o banco
    'user': 'root',
    'password': 'password',
    'database': 'wines_db'
}

@app.route('/wines', methods=['GET'])
def get_wines():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM wines")
    result = cursor.fetchall()
    conn.close()
    return jsonify(result)

@app.route('/wines', methods=['POST'])
def add_wine():
    data = request.json
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO wines (name, type, region, year, price) VALUES (%s, %s, %s, %s, %s)", 
                   (data['name'], data['type'], data['region'], data['year'], data['price']))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Wine added!'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
