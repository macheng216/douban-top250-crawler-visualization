# save_data.py
import pandas as pd

def save_to_csv(data, filename="douban_top250.csv"):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding="utf-8-sig")
    print(f"✅ 已保存到 {filename}")