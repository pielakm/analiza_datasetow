from orm import Table
import json
class PriceData(Table):
        table_name = 'price_data2'
# Read data from the JSON file
with open('./DATA/commodity_prices_filtered.json', 'r') as json_file:
    data = json.load(json_file)



try: 
    Table.connect(config_dict={
    'host': 'aplikacja-konwentowa-aplikacja-konwentowa.a.aivencloud.com',
    'port': 11334,
    'user': 'piotr',
    'password': 'AVNS_ntXfs4l983OUh5HbRr_',
    'database': 'integracja'
    })
    for record in data:
        new_price_data = PriceData(priceid=record['priceid'], date=record['date'], oil_brent=record['oil_brent'], oil_dubai=record['oil_dubai'], coffee_arabica=record['coffee_arabica'], coffee_robustas=record['coffee_robustas'], tea_columbo=record['tea_columbo'], tea_kolkata=record['tea_kolkata'], tea_mombasa=record['tea_mombasa'], sugar_eu=record['sugar_eu'], sugar_us=record['sugar_us'], sugar_world=record['sugar_world'])
        new_price_data.save()
    
except Exception as e:
     print(f"Error: {e}")