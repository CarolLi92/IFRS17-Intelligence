def build_insight(df):
    return df.head(3).to_dict('records')
