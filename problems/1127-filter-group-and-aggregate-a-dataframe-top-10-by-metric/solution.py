import pandas as pd

def solution(df):
    df = df[df['status'] == 'completed']
    df = df.groupby('region')['amount'].sum().sort_values(ascending = False).head(10).reset_index()
    return df
