# The Opioid Gap: Data Processing & Methodology

This repository contains the underlying data, extraction scripts, and methodological documentation for **"The Opioid Gap"** project. The project provides a comparative analysis of the opioid crisis in the USA and Europe, focusing on historical drivers (the advertising anomaly in the USA) and emerging threats (the rise of nitazenes in the EU).

## 📊 Data Sources

The data used in this analysis were sourced from the following institutions:

* **USA Mortality & Prescriptions:** [CDC WONDER](https://wonder.cdc.gov/) (Centers for Disease Control and Prevention). Mortality data correspond to ICD-10 codes (T40.1–T40.4, T40.6).
* **European Mortality & Trends:** [EMCDDA](https://www.emcdda.europa.eu/) (European Monitoring Centre for Drugs and Drug Addiction) – European Drug Report 2024.
* **Seizures:** [UNODC](https://dataunodc.un.org/) (United Nations Office on Drugs and Crime) – World Drug Report.
* **Geodata:** Natural Earth (administrative boundaries for countries and US states).

## 🛠️ Data Processing Pipeline

The processing workflow consisted of several stages:

1.  **Extraction and Cleaning (Python):** Raw data from CDC and EMCDDA were extracted and cleaned using scripts located in the `/scripts` directory. The `pandas` library was utilized to standardize state/country names and handle missing values.
2.  **Normalization:** To ensure comparability, mortality data were normalized to a rate of **per 100,000 inhabitants** (Crude Rate).
3.  **Attribute Join:** Cleaned data were joined with vector layers in **QGIS 3.x** using unique ISO country codes and US FIPS state codes.
4.  **Visualization:** * Main choropleth maps use the **Natural Breaks (Jenks)** classification method.
    * Prescription intensity was visualized using **Rule-based symbology** (variable density hatching).
    * Charts were generated in LibreOffice Draw and exported as **SVG** (converted to curves to ensure rendering integrity in QGIS).

## ⚠️ Methodological Notes

When comparing the USA and Europe, several critical methodological differences had to be addressed:

* **Prescription Metrics:** The USA reports data as *number of prescriptions per 100 residents* (Rx per 100), whereas Europe uses *Standard Defined Daily Doses* (S-DDD per 1 million inhabitants/day). The poster utilizes a dual legend to allow for the correct interpretation of both metrics simultaneously.
* **The Synthetic Shift (Nitazenes):** The analysis in the bottom-right section of the poster visualizes the increasing diversification of the EU market. Following the decrease in opium production in Afghanistan, there has been a significant rise in synthetic opioids (specifically nitazenes such as isotonitazene and protonitazene) since 2023, which are significantly more potent than heroin.

## 📂 Repository Structure

* `/data`: Final CSV tables used for QGIS import.
* `/scripts`: Python scripts for data extraction (Web Scraping / API calls).
* `/maps`: Exported map views and legend components.
* `README.md`: This methodological overview.

---

**Author:** [Your Name]  
**Project:** Cartographic Visualization of Global Health Threats  
**Tools:** QGIS 3.34, Python (Pandas), LibreOffice Calc/Draw
