import pandas as pd

def solution(df1, df2, df3):
    
    df4 = pd.merge(left = df1, right = df2, on = 'emp_id', how = 'inner')

    df5 = pd.merge(left = df4, right = df3, on = 'emp_id', how = 'left')

    return df5
