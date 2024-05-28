import csv
import xml.etree.ElementTree as ET

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
                child.text = row[field]

    # Create a tree object from the root element
    tree = ET.ElementTree(root)

    # Write the tree to the XML file
    tree.write(xml_file_path, encoding='utf-8', xml_declaration=True)

# Example usage
csv_file_path = 'example.csv'
xml_file_path = 'output.xml'
csv_to_xml(csv_file_path, xml_file_path)
