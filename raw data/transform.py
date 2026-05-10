import pandas as pd

# 1. Načtení souboru
file_path = 'nationwide-drugs-fy22-fy25.csv'
df = pd.read_csv(file_path)

# 2. Čištění názvů Area of Responsibility (odstranění přípon FIELD OFFICE a SECTOR)
def clean_aor(name):
    if pd.isna(name): return name
    return name.replace(' FIELD OFFICE', '').replace(' SECTOR', '').strip().title()

df['Clean_AOR'] = df['Area of Responsibility'].apply(clean_aor)

# 3. Definice mapování AOR -> Stát USA
aor_to_state = {
    'Tucson': 'Arizona', 'Yuma': 'Arizona',
    'San Diego': 'California', 'El Centro': 'California', 'San Francisco': 'California', 'Los Angeles': 'California',
    'Laredo': 'Texas', 'El Paso': 'Texas', 'Rio Grande Valley': 'Texas', 'Del Rio': 'Texas', 'Big Bend': 'Texas', 'Houston': 'Texas',
    'Miami': 'Florida', 'Tampa': 'Florida',
    'Buffalo': 'New York', 'New York City': 'New York', 'New York': 'New York',
    'Detroit': 'Michigan',
    'Seattle': 'Washington', 'Blaine': 'Washington', 'Spokane': 'Washington',
    'Boston': 'Massachusetts', 'Baltimore': 'Maryland', 'New Orleans': 'Louisiana', 'Chicago': 'Illinois',
    'Atlanta': 'Georgia', 'Portland': 'Oregon', 'San Juan': 'Puerto Rico', 'Houlton': 'Maine', 'Swanton': 'Vermont',
    'Havre': 'Montana', 'Grand Forks': 'North Dakota', 'Newark': 'New Jersey', 'St. Louis': 'Missouri'
}

df['State'] = df['Clean_AOR'].map(aor_to_state)

# 4. Filtrace (Pouze OFO/USBP a Fentanyl/Heroin)

valid_drugs = ['Fentanyl', 'Heroin']
df_filtered = df[(df['Drug Type'].isin(valid_drugs))].copy()

# 5. Převod na kilogramy (1 lb = 0.453592 kg)
df_filtered['Qty_kg'] = df_filtered['Sum Qty (lbs)'] * 0.45359237

# 6. Agregace dat pro Small Multiples (2021, 2023, 2024)
years_to_extract = [2021, 2023, 2024]
final_export = df_filtered[df_filtered['FY'].isin(years_to_extract)].groupby(['FY', 'State', 'Drug Type'])['Qty_kg'].sum().unstack(fill_value=0).reset_index()
final_export['Total_kg'] = final_export['Fentanyl'] + final_export['Heroin']

# 7. Uložení výsledku pro QGIS
final_export.to_csv('usa_opioid_seizures_qgis1.csv', index=False)
print("Soubor 'usa_opioid_seizures_qgis.csv' byl úspěšně vytvořen.")