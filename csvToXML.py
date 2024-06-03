import csv
import xml.etree.ElementTree as ET
from datetime import datetime

def format_date(date_str):
    try:
        # Parse the date string
        date = datetime.strptime(date_str, '%Y-%m-%d')
        # Return the formatted date string
        return date.strftime('%Y-%m-%d')
    except ValueError:
        # Handle invalid dates (e.g., '1970-1-0')
        parts = date_str.split('-')
        year = parts[0]
        month = parts[1] if parts[1] != '0' else '01'
        day = parts[2] if parts[2] != '0' else '01'
        return f"{year}-{month.zfill(2)}-{day.zfill(2)}"

def csv_to_xml(csv_file_path, xml_file_path):
    # Create the root element
    root = ET.Element('data')

    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            # Create an 'event' element for each row
            event = ET.SubElement(root, 'event')
            for field in reader.fieldnames:
                # Create a child element for each field
                child = ET.SubElement(event, field)
                if field == 'date':
                    # Format the date before adding it to the XML
                    child.text = format_date(row[field])
                else:
                    child.text = row[field]

    # Create a tree object from the root element
    tree = ET.ElementTree(root)

    # Write the tree to the XML file
    tree.write(xml_file_path, encoding='utf-8', xml_declaration=True)
# Example usage
csv_file_path = './DATA/globalterrorismdb_filtered.csv'
xml_file_path = './DATA/globalterrorismdb_filtered.xml'
csv_to_xml(csv_file_path, xml_file_path)
