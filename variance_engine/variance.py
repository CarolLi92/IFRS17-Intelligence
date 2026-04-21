def calculate_variance(df):
    df=df.copy(); df['prev']=df.groupby(['entity','metric'])['value'].shift(1); df['variance']=df['value']-df['prev']; return df
