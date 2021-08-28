import pandas as pd

def friendly_table_outputter(array, a, b):
    df = pd.DataFrame(array)
    df=df.set_index([list(a)])
    df=df.set_axis([list(b)], axis=1)
    
#     print(df, '\n')
    return df