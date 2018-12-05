import pandas as pd
import numpy as np

df = pd.read_csv('cleaned_intersections.csv')
sp_df = pd.read_csv('s_to_sp.csv')

concat_df = pd.merge(df, sp_df, on='CNN')

print concat_df

concat_df.to_csv("cleaned_intersections_with_sp.csv")