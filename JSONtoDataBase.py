import pymysql
import json

# Read data from the JSON file
with open('./DATA/commodity_prices_filtered.json', 'r') as json_file:
    data = json.load(json_file)

# Database connection details
connection_params = {
    "host": "aplikacja-konwentowa-aplikacja-konwentowa.a.aivencloud.com",
    "port": 11334,
    "user": "piotr",
    "password": "AVNS_ntXfs4l983OUh5HbRr_",
    "db": "integracja",
    "charset": "utf8mb4",
    "cursorclass": pymysql.cursors.DictCursor,
}

# Establish a connection
try:
    connection = pymysql.connect(**connection_params)
    cur = connection.cursor()

    # Insert data
    for record in data:
        insert_query = """
        INSERT INTO price_data (priceid, date, oil_brent, oil_dubai, coffee_arabica, coffee_robustas, tea_columbo, tea_kolkata, tea_mombasa, sugar_eu, sugar_us, sugar_world)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        cur.execute(insert_query, (
            record['priceid'],
            record['date'],
            record['oil_brent'],
            record['oil_dubai'],
            record['coffee_arabica'],
            record['coffee_robustas'],
            record['tea_columbo'],
            record['tea_kolkata'],
            record['tea_mombasa'],
            record['sugar_eu'],
            record['sugar_us'],
            record['sugar_world']
        ))

    # Commit changes and close the connection
    connection.commit()
    cur.close()
    connection.close()
    print("Data inserted successfully!")

except pymysql.Error as e:
    print(f"Error: {e}")
