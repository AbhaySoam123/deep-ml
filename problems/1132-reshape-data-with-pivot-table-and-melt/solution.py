import pandas as pd

def solution(df):
    df_pivot = df.pivot_table(index = 'date', columns = 'product', values = 'sales', aggfunc = 'sum', fill_value = 0)

    df_new = df_pivot.reset_index().melt(id_vars = 'date', var_name = 'product', 
    value_name = 'sales').sort_values(by = ['date', 'product'], ascending = [True, True]).reset_index(drop = True)

    return df_new