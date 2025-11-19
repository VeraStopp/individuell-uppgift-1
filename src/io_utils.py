import pandas as pd

def load_data(filepath):
    """
    Load CSV file and clean the column names.
    """
    df = pd.read_csv(filepath)
    df.columns = (df.columns.str.strip().str.replace(" ", "_").str.lower())
    return df