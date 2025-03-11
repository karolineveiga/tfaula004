from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Database connection configuration
db_config = {
    'user': 'root',
    'password': '',
    'host': 'db',  # Use 'db' as the service name defined in docker-compose
    'database': 'basedeAlunos'
}

def get_db_connection():
    connection = mysql.connector.connect(**db_config)
    return connection

@app.route('/consulta', methods=['GET'])
def consulta():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    
    query = "SELECT * FROM Alunos"
    cursor.execute(query)
    results = cursor.fetchall()
    
    cursor.close()
    connection.close()
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)