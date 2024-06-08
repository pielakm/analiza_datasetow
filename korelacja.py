
import pandas as pd
import xml.etree.ElementTree as ET
def correlation():
    # Load the dataset from XML file
    data_terrorism = pd.read_xml('./DATA/globalterrorismdb_filtered.xml')

    # Convert 'date' column to datetime type
    data_terrorism['date'] = pd.to_datetime(data_terrorism['date'], format='%Y-%m-%d', errors='coerce')

    # Extract year from the 'date' column and count the number of attacks per date
    attacks_by_date = data_terrorism['date'].value_counts().sort_index().rename("attacks")

    # Read the CSV file into a DataFrame
    df_commodities = pd.read_csv("./DATA/commodity_prices_filtered.csv", index_col="date", parse_dates=True, encoding='utf-8')

    # Prepare the oil price data
    oil_prices = df_commodities["oil_dubai"].rename("oil_price")

    # Merge the two datasets on the date index
    merged_data = pd.concat([attacks_by_date, oil_prices], axis=1).fillna(0)

    # Calculate the correlation between number of attacks and oil prices
    correlations = merged_data['attacks'].rolling(window=30).corr(merged_data['oil_price'].shift(30)).dropna()

    # Find the highest correlations
    highest_correlations = correlations.abs().nlargest(10)

    results = []

    for date, correlation in highest_correlations.items():
        approximate_date_of_increase = date + pd.Timedelta(days=45)
        result = {
            'date_of_attack': date.strftime('%Y-%m-%d'),
            'correlation': correlation,
            'approximate_date_of_increase': approximate_date_of_increase.strftime('%Y-%m-%d')
        }
        results.append(result)
        print(f"Date of attack: {date}")
        print(f"Correlation: {correlation}")
        print(f"Approximate date of oil price increase: {approximate_date_of_increase}\n")

    # Save results to JSON
    import json
    with open('./RESULTS/results_correlacion.json', 'w') as json_file:
        json.dump(results, json_file, indent=4)

    # Save results to XML
    root = ET.Element("results")

    for result in results:
        result_elem = ET.SubElement(root, "result")
        date_of_attack_elem = ET.SubElement(result_elem, "date_of_attack")
        date_of_attack_elem.text = result['date_of_attack']
        correlation_elem = ET.SubElement(result_elem, "correlation")
        correlation_elem.text = str(result['correlation'])
        approximate_date_of_increase_elem = ET.SubElement(result_elem, "approximate_date_of_increase")
        approximate_date_of_increase_elem.text = result['approximate_date_of_increase']

    tree = ET.ElementTree(root)
    tree.write("./RESULTS/results_correlacion.xml")
