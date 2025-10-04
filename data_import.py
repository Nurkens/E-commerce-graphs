import pandas as pd
from config import DATASETS_DIR, ENGINE
from pathlib import Path

def import_all_csv():
    csv_files = list(Path(DATASETS_DIR).glob("*.csv"))
    if not csv_files:
        print("Нет CSV файлов в datasets/.")
        return
    for csv in csv_files:
        table_name = csv.stem.lower()
        print(f"Импортирую {csv.name} -> таблица `{table_name}`")
        try:
            df = pd.read_csv(csv, low_memory=False)
        except Exception:
            df = pd.read_csv(csv, sep=";", low_memory=False)
        df.columns = [c.strip().lower() for c in df.columns]
        try:
            df.to_sql(table_name, ENGINE, if_exists="replace", index=False, method="multi", chunksize=1000)
            print(f" → {len(df)} строк записано в `{table_name}`")
        except Exception as e:
            print(f"Ошибка импорта {csv}: {e}")

if __name__ == "__main__":
    import_all_csv()
