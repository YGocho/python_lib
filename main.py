import pandas as pd
import numpy as np

def getValueIndex(df, val):
    print("getValueIndex")

    df_wk = df.copy()

    idx = df_wk[df_wk['key1'] >= val].head(1).index

    print(idx)

    return idx


if __name__ == '__main__':
    print("AAA")

    dic = {'key1': [1, 2, 3, 4, 5, 6, 7, 8, 9], 'key2': ['A','B','C','D','E','F','G','H','I']}

    df = pd.DataFrame.from_dict(dic)

    print(df)

    idx = getValueIndex(df, 5)

    val = df.loc[idx,'key1']
    print(val)

