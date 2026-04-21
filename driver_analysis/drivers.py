def rank_drivers(df):
    return df.sort_values('variance',ascending=False)
