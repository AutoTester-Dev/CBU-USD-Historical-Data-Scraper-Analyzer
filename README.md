# CBU USD Historical Data Scraper & Analyzer

A Python-based tool designed to automatically fetch, process, and analyze historical USD/UZS exchange rates from the Central Bank of Uzbekistan (CBU) API.

## 🚀 Features
* **Automated Data Scraping:** Iterates through multi-year date ranges to query daily official exchange rates via the official CBU JSON API.
* **Data Cleaning & Exporting:** Uses `pandas` to structure time-series data and exports it into a clean, ready-to-use CSV file (`dollar_historik_2024_2026.csv`).
* **Error Handling:** Built-in exception handling and timeouts to manage network latency and server response stability.

## 🛠️ Tech Stack
* **Python** (`requests`, `pandas`, `datetime`, `time`)
* **Google Colab** (Cloud development environment)
* **CBU Open API** (Data source)

## 📁 File Structure
* `cbu_scraper.py` — The core script used for fetching data.
* `dollar_historik_2024_2026.csv` — The collected dataset containing daily rates.

## 📊 Quick Dataset Overview
* **Time Range:** Dec 2023 – Sep 2026 (~962 records)
* **Average Rate:** ~12,478.59 UZS
* **Max Rate:** 13,003.95 UZS (Feb 14, 2025)
* **Min Rate:** 11,778.52 UZS (Aug 26, 2026)

## 💻 Usage
Run the script to collect fresh data or process the existing CSV file for financial trend analysis and data visualization.
