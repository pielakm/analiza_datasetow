import xml.etree.ElementTree as ET
import pymysql

# Give the connection parameters
conn = pymysql.connect(
    user='mateusz',
    password='AVNS_98ZhacpZ07OS_0v-RKI',
    port=11334,
    host='aplikacja-konwentowa-aplikacja-konwentowa.a.aivencloud.com',
    database='integracja',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# Create table if it doesn't exist
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
# Creating the cursor object
with conn.cursor() as c:
    c.execute(create_table_query)
    conn.commit()

# Reading XML file
tree = ET.parse('./DATA/globalterrorismdb_filtered.xml')
root = tree.getroot()

# Retrieving the data and inserting into table
for i, j in zip(root.findall('event'), range(1, len(root.findall('event')) + 1)):
    country_txt = i.find('country_txt').text
    region_txt = i.find('region_txt').text
    city = i.find('city').text
    date = i.find('date').text
    eventid = i.find('eventid').text

    # SQL query to insert data into database
    data = """INSERT INTO global_terrorism (country_txt, region_txt, city, date, eventid)
              VALUES (%s, %s, %s, %s, %s)"""

    # Executing cursor object
    with conn.cursor() as c:
        c.execute(data, (country_txt, region_txt, city, date, eventid))
        conn.commit()
    # print("Event No-", j, "stored successfully")

# Closing the connection
conn.close()
