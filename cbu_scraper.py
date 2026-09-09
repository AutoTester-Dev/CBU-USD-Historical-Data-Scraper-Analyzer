import pandas as pd
import requests
from datetime import datetime
import time

def fetch_exchange_rates():
    # Sana oralig'ini belgilaymiz (2024-yil 1-yanvardan bugungi kungacha)
    start_date = datetime(2024, 1, 1)
    end_date = datetime.now()
    
    date_list = pd.date_range(start=start_date, end=end_date)
    data = []

    print("CBU API'dan ma'lumotlar yig'ish boshlandi...")

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
            print(f"Xatolik {date_str} sanasida: {e}")
        
        # Serverga ortiqcha yuklama bermaslik uchun kichik tanaffus
        time.sleep(0.05)

    # DataFrame ga o'tkazamiz va CSV faylga yozamiz
    df = pd.DataFrame(data)
    csv_filename = 'dollar_historik_2024_2026.csv'
    df.to_csv(csv_filename, index=False, encoding='utf-8-sig')

    print(f"Muvaffaqiyatli yakunlandi! Jami {len(df)} ta kunlik ma'lumot '{csv_filename}' fayliga saqlandi.")

if __name__ == "__main__":
    fetch_exchange_rates()
