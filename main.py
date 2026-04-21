import pandas as pd
from data_processing.standardize import standardize_data
from variance_engine.variance import calculate_variance
from semantic_layer.mapping import apply_semantic_mapping
from driver_analysis.drivers import rank_drivers
from insight_builder.builder import build_insight

df=pd.read_csv('examples/mock_data.csv')
df=standardize_data(df)
df=calculate_variance(df)
df=apply_semantic_mapping(df)
df=rank_drivers(df)
print(build_insight(df))
