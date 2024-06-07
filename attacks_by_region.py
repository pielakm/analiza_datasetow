import xml.etree.ElementTree as ET
import pandas as pd
import matplotlib.pyplot as plt


def attacks_by_region():
    # Load data from XML
    tree = ET.parse('./DATA/globalterrorismdb_filtered.xml')
    root = tree.getroot()

    # Extract data into a DataFrame
    conflict_data = []
    for event in root.findall('event'):
        region = event.find('region_txt').text
        conflict_data.append({'region': region})

    df_conflicts = pd.DataFrame(conflict_data)

    # Count the number of attacks in each region
    conflict_counts_by_region = df_conflicts['region'].value_counts().sort_index().reset_index()
    conflict_counts_by_region.columns = ['region', 'num_attacks']

    # Create a Figure
    fig, ax = plt.subplots(figsize=(14, 8))

    # Plot bar chart of the number of attacks in each region
    ax.bar(conflict_counts_by_region['region'], conflict_counts_by_region['num_attacks'], color='skyblue')
    ax.set_title('Number of Attacks in Different Regions')
    ax.set_xlabel('Region')
    ax.set_ylabel('Number of Attacks')
    ax.set_xticks(range(len(conflict_counts_by_region['region'])))
    ax.set_xticklabels(conflict_counts_by_region['region'], rotation=45, ha='right')
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    return fig

