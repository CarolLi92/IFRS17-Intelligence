SEMANTIC_MAP={'revenue':'insurance revenue'}

def apply_semantic_mapping(df):
    df=df.copy(); df['label']=df['metric'].map(SEMANTIC_MAP).fillna(df['metric']); return df
