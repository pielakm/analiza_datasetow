import pandas as pd

# Load the CSV file
csv_file_path = './DATA/commodity_prices_filtered.csv'  # The path to the uploaded CSV file
df = pd.read_csv(csv_file_path)

# Convert the DataFrame to JSON format
json_data = df.to_json(orient='records', date_format='iso')

# Save the JSON data to a file
json_file_path = './DATA/commodity_prices_filtered.json'
with open(json_file_path, 'w') as json_file:
    json_file.write(json_data)

print(f"Data has been successfully converted to JSON and saved to {json_file_path}")
