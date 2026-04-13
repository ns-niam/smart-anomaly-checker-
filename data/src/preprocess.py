import pandas as pd

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print("Error loading data:", e)
        return None


def clean_data(df):
    # remove null values
    df = df.dropna()

    # ensure numeric
    df['value'] = pd.to_numeric(df['value'], errors='coerce')
    df = df.dropna()

    return df
