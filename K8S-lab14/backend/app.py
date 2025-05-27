from flask import Flask, request, render_template, jsonify, redirect
import mysql.connector
import os

app = Flask(__name__)

# Connect to MySQL database
def get_db_connection():
    conn = mysql.connector.connect(
        host=os.getenv('MYSQL_HOST', 'mysql'),
        database=os.getenv('MYSQL_DB', 'winecollection'),
        user=os.getenv('MYSQL_USER', 'root'),
        password=os.getenv('MYSQL_PASSWORD', 'yourpassword')
    )
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wines', methods=['GET'])
def get_wines():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM wines')
    wines = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(wines)

@app.route('/add', methods=['POST'])
def add_wine():
    name = request.form['name']
    year = request.form['year']
    wine_type = request.form['type']
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO wines (name, year, type) VALUES (%s, %s, %s)', (name, year, wine_type))
    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
