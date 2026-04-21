import pandas as pd

def standardize_data(df):
    df=df.copy(); df.columns=[c.lower() for c in df.columns]; return df
