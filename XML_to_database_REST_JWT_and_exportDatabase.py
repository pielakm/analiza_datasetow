from flask import Flask, jsonify, request
import pymysql
import xml.etree.ElementTree as ET
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import csv

app = Flask(__name__)

# Konfiguracja połączenia z lokalną bazą danych
db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'integracja',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

conn = pymysql.connect(**db_config)

# Konfiguracja JWT
app.config['JWT_SECRET_KEY'] = 'SecretKey1012577937423573498527345845983448538322'  # Zmień na swój własny klucz tajny
jwt = JWTManager(app)

# Tworzenie tabeli, jeśli nie istnieje
create_table_query = """
CREATE TABLE IF NOT EXISTS global_terrorism (
    id INT AUTO_INCREMENT PRIMARY KEY,
    country_txt VARCHAR(255),
    region_txt VARCHAR(255),
    city VARCHAR(255),
    date DATE,
    eventid INT
);
"""

with conn.cursor() as c:
    c.execute(create_table_query)
    conn.commit()

# Funkcja ustawiająca poziom izolacji
def set_isolation_level(conn, level):
    with conn.cursor() as cursor:
        cursor.execute(f"SET SESSION TRANSACTION ISOLATION LEVEL {level};")
    conn.commit()

# Endpoint do logowania
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        if data is None:
            raise ValueError("No JSON data received")

        username = data.get('username', None)
        password = data.get('password', None)

        # Simple user check (for demonstration purposes, use a database in real applications)
        if username != 'root' or password != '':
            return jsonify({"msg": "Bad username or password"}), 401

        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)

    except ValueError as e:
        return jsonify({"msg": str(e)}), 400
    except Exception as e:
        return jsonify({"msg": "Failed to decode JSON object: " + str(e)}), 400

# Endpoint do ładowania danych z XML, wymaga uwierzytelnienia
@app.route('/load_from_xml', methods=['POST'])
@jwt_required()
def load_from_xml():
    try:
        # Ustawienie poziomu izolacji
        set_isolation_level(conn, 'REPEATABLE READ')

        # Wczytywanie pliku XML
        tree = ET.parse('./DATA/globalterrorismdb_filtered.xml')
        root = tree.getroot()

        # Pobieranie danych i wstawianie do tabeli
        with conn.cursor() as cursor:
            cursor.execute("START TRANSACTION;")
            for event in root.findall('event'):
                country_txt = event.find('country_txt').text
                region_txt = event.find('region_txt').text
                city = event.find('city').text
                date = event.find('date').text
                eventid = event.find('eventid').text

                # SQL query do wstawiania danych
                query = """INSERT INTO global_terrorism (country_txt, region_txt, city, date, eventid)
                           VALUES (%s, %s, %s, %s, %s)"""

                cursor.execute(query, (country_txt, region_txt, city, date, eventid))
            conn.commit()

        return jsonify({'message': f'Added into database: {db_config["database"]}'}), 201

    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)}), 500
@app.route('/export_to_csv', methods=['GET'])
@jwt_required()
def export_to_csv():
    try:
        # Select data from the database
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM global_terrorism")
            data = cursor.fetchall()

        # Write data to CSV file
        with open('./RESULTS/exported_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'country_txt', 'region_txt', 'city', 'date', 'eventid']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)

        return jsonify({'message': 'Data exported to exported_data.csv'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route('/count_events', methods=['GET'])
@jwt_required()
def count_events():
    try:
        # Wykonanie zapytania do bazy danych
        with conn.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) AS count FROM global_terrorism")
            result = cursor.fetchone()

        return jsonify({'count': result['count']}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)


