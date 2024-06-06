import xml.etree.ElementTree as ET
import pandas as pd
import matplotlib.pyplot as plt

# Wczytaj dane z XML
tree = ET.parse('./DATA/globalterrorismdb_filtered.xml')
root = tree.getroot()

# Wyodrębnij dane do DataFrame
conflict_data = []
for event in root.findall('event'):
    region = event.find('region_txt').text
    conflict_data.append({'region': region})

df_conflicts = pd.DataFrame(conflict_data)

# Policz liczbę ataków w każdym regionie
conflict_counts_by_region = df_conflicts['region'].value_counts().sort_index().reset_index()
conflict_counts_by_region.columns = ['region', 'num_attacks']
# Wykres kolumnowy liczby ataków w poszczególnych regionach
plt.figure(figsize=(14, 8))
plt.bar(conflict_counts_by_region['region'], conflict_counts_by_region['num_attacks'], color='skyblue')
plt.title('Liczba ataków w poszczególnych regionach')
plt.xlabel('Region')
plt.ylabel('Liczba ataków')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
