import pandas as pd
import requests
from datetime import datetime
import time

def fetch_exchange_rates():
    # Define date range from Jan 1, 2024 to present
    start_date = datetime(2024, 1, 1)
    end_date = datetime.now()
    
    date_list = pd.date_range(start=start_date, end=end_date)
    data = []

    print("Data fetching from CBU API started...")

    for single_date in date_list:
        date_str = single_date.strftime('%Y-%m-%d')
        url = f"https://cbu.uz/uz/arkhiv-kursov-valyut/json/USD/{date_str}/"
        
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                res_json = response.json()
                if len(res_json) > 0:
                    item = res_json[0]
                    data.append({
                        'Date': item.get('Date'),
                        'Ccy': item.get('Ccy'),
                        'CcyNm_UZ': item.get('CcyNm_UZ'),
                        'Rate': float(item.get('Rate', 0))
                    })
        except Exception as e:
            print(f"Error on date {date_str}: {e}")
        
        # Brief pause to prevent server overload
        time.sleep(0.05)

    # Convert to DataFrame and export to CSV
    df = pd.DataFrame(data)
    csv_filename = 'dollar_historik_2024_2026.csv'
    df.to_csv(csv_filename, index=False, encoding='utf-8-sig')

    print(f"Successfully completed! Total {len(df)} daily records saved to '{csv_filename}'.")

if __name__ == "__main__":
    fetch_exchange_rates()
                                        
