import pandas as pd

def solution(df):

    # Dropping columns
    col_to_drop = df.isnull().mean()
    df = df.loc[:, col_to_drop <=0.5]
   
    # Dropping rows
    row_to_drop = df.isnull().mean(axis = 1)
    df = df.loc[row_to_drop<=0.5, :]

    # Selecting Numeric Columns
    numeric_cols = df.select_dtypes(include = 'number').columns
    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

    # Selecting Non - Numeric Columns

    non_numeric_cols = df.select_dtypes(exclude = 'number').columns
    
    for col in non_numeric_cols:
        mode = df[col].mode()
        if not mode.empty:
            df[col] = df[col].fillna(mode.iloc[0])
    
    df = df.reset_index(drop = True)

    return df


