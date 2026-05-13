# The Opioid Gap: Data Processing & Methodology

This repository contains the underlying data, extraction scripts, and methodological documentation for **"The Opioid Gap"** project. The project provides a comparative analysis of the opioid crisis in the USA and Europe, focusing on historical drivers (the advertising anomaly in the USA) and emerging threats (the rise of nitazenes in the EU).

## 📊 Data Sources

The data used in this analysis were sourced from the following institutions:

* **USA Mortality & Prescriptions:** [CDC WONDER](https://wonder.cdc.gov/) (Centers for Disease Control and Prevention). Mortality data correspond to ICD-10 codes (T40.1–T40.4, T40.6).
* **USA Seizures:** [CBP](https://www.cbp.gov/document/stats/nationwide-drug-seizures) (U.S. Customs and Border Protection).
* **European Mortality & Seizures:** [EUDA](https://www.euda.europa.eu/) (European Union Drug Agency) – European Drug Report 2025, Statistical Bulletin 2025.
* **European Prescriptions:** [OECD](https://data-explorer.oecd.org/vis?lc=en&df[ds]=dsDisseminateFinalDMZ&df[id]=DSD_HCQO%40DF_PIPC&df[ag]=OECD.ELS.HD&dq=.A.PROPOUDD.DDD_10P3HB.Y_GE18._T.OBS..&pd=2009%2C2024&to[TIME_PERIOD]=false&vw=tb) (The Organization for Economic Cooperation and Development).
* **European Populations:** [EUROSTAT](https://ec.europa.eu/eurostat/databrowser/view/demo_pjanbroad/default/table?lang=en) (Population for Crude Rate calculation).
* **Geodata:** [Natural Earth](https://www.naturalearthdata.com/) (administrative boundaries for countries and US states).
* **Images:** [DEA](https://www.dea.gov/) (Drug Enforcement Administration), [Wikipedia](https://www.wikipedia.org), [Google Gemini](https://gemini.google.com)

## 🛠️ Data Processing Pipeline

The processing workflow consisted of several stages:

1.  **Extraction and Cleaning (Python):** Raw data from CDC were extracted and cleaned using scripts located in the `/raw data` directory. The `pandas` library was utilized to standardize state/country names and handle missing values.
2.  **Normalization:** To ensure comparability, mortality data were normalized to a rate of **per 100,000 inhabitants** (Crude Rate).
3.  **Attribute Join:** Cleaned data were joined with vector layers in **QGIS 3.44.7** using unique ISO country codes.
4.  **Visualization:**
    * Prescription intensity was visualized using **Rule-based symbology** (variable density patterns).
    * The chart was generated in LibreOffice Calc and exported in LibreOffice Draw as **SVG**.

## ⚠️ Methodological Notes

When comparing the USA and Europe, the critical methodological differences had to be addressed:

* **Prescription Metrics:** The USA reports data as *number of prescriptions per 100 residents* (Rx per 100), whereas Europe uses *Defined Daily Doses* (DDD per 1000 inhabitants/day). The poster utilizes a dual legend to allow for the correct interpretation of both metrics simultaneously.
* **Temporal Scope:** Map visualizations represent data for the reference year 2023. For jurisdictions where 2023 metrics were not available, the latest available figures preceding 2023 were utilized to ensure maximum geographic coverage.
## 📂 Repository Structure

* `/images`: Images that were used in the map.
* `/processed data`: Final CSV tables used for QGIS import.
* `/raw data`: Raw tables downloaded from the sources and the script for processing.
* `readme.md`: This methodological overview.
* `the opioid gap.pdf`: The final map.

---

* **Author:** Bc. Mykhailo Rachenko
* **Project:** 155PKAR at CTU in Prague
* **Tools:** QGIS 3.44.7, Python (Pandas), LibreOffice Calc/Draw
