import xml.etree.ElementTree as ET
import pandas as pd
import matplotlib.pyplot as plt

# Wczytaj dane z XML
tree = ET.parse('./DATA/globalterrorismdb_filtered.xml')
root = tree.getroot()

# Wyodrębnij dane do DataFrame
conflict_data = []
for event in root.findall('event'):
    date = event.find('date').text
    year = date.split('-')[0]
    conflict_data.append({'year': year})

df_conflicts = pd.DataFrame(conflict_data)
df_conflicts['year'] = df_conflicts['year'].astype(int)

# Policz liczbę ataków w każdym roku
conflict_counts = df_conflicts['year'].value_counts().sort_index().reset_index()
conflict_counts.columns = ['year', 'num_attacks']

# Wykres liczby ataków w czasie
plt.figure(figsize=(12, 6))
plt.plot(conflict_counts['year'], conflict_counts['num_attacks'], marker='o')
plt.title('Liczba ataków w czasie')
plt.xlabel('Rok')
plt.ylabel('Liczba ataków')
plt.grid(True)
plt.show()
