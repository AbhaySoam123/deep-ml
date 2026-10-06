import pandas as pd


def solution(df):
    # TODO: bucket scores, count per (grade, bucket), cumulative percentage within grade
    df['bucket'] = (df['score']//10)*10
    
    df = df.groupby(['grade', 'bucket']).size().reset_index(name='count').sort_values(by = ['grade','bucket'], ascending = [True, True])

    df['cum_count'] = df.groupby('grade')['count'].cumsum()

    df['cum_pct'] = (df['cum_count']/ df.groupby('grade')['count'].transform('sum')* 100).round(2)

    df = df[['grade', 'bucket', 'count', 'cum_pct']]

    return df

  
