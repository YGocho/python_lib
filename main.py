import pandas as pd
import numpy as np

def getGEValueIndex(df, key, val):
    return df[df[key] >= val].head(1).index


if __name__ == '__main__':

    dic = {'key1': [1, 2, 3, 4, 5, 6, 7, 8, 9], 'key2': ['A','B','C','D','E','F','G','H','I']}

    df = pd.DataFrame.from_dict(dic)

    print(df)

    idx = getGEValueIndex(df, 'key1', 5)

    val = df.loc[idx,'key1'] #
    print(val)


