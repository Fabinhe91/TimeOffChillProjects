from flask import Flask, jsonify, request
import psycopg2
import os

app = Flask(__name__)

# Database connection function
def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('POSTGRES_HOST'),
        database=os.getenv('POSTGRES_DB'),
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD')
    )
    return conn

# Get all wines
@app.route('/wines', methods=['GET'])
def get_wines():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM wines;')
    wines = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify(wines)

# Add a new wine
@app.route('/wines', methods=['POST'])
def add_wine():
    data = request.get_json()
    name = data['name']
    year = data['year']
    type_ = data['type']

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO wines (name, year, type) VALUES (%s, %s, %s)', (name, year, type_))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Wine added!"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
