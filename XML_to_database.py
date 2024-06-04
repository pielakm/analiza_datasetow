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
    provstate VARCHAR(255),
    city VARCHAR(255),
    summary TEXT,
    attacktype1_txt VARCHAR(255),
    attacktype2_txt VARCHAR(255),
    targtype1_txt VARCHAR(255),
    targsubtype1_txt VARCHAR(255),
    motive TEXT,
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
    provstate = i.find('provstate').text
    city = i.find('city').text
    summary = i.find('summary').text if i.find('summary') is not None else None
    attacktype1_txt = i.find('attacktype1_txt').text
    attacktype2_txt = i.find('attacktype2_txt').text if i.find('attacktype2_txt') is not None else None
    targtype1_txt = i.find('targtype1_txt').text
    targsubtype1_txt = i.find('targsubtype1_txt').text
    motive = i.find('motive').text if i.find('motive') is not None else None
    date = i.find('date').text
    eventid = i.find('eventid').text

    # SQL query to insert data into database
    data = """INSERT INTO global_terrorism (country_txt, region_txt, provstate, city, summary, attacktype1_txt, attacktype2_txt, targtype1_txt, targsubtype1_txt, motive, date, eventid)
              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    # Executing cursor object
    with conn.cursor() as c:
        c.execute(data, (country_txt, region_txt, provstate, city, summary, attacktype1_txt, attacktype2_txt, targtype1_txt, targsubtype1_txt, motive, date, eventid))
        conn.commit()
    # print("Event No-", j, "stored successfully")

# Closing the connection
conn.close()
