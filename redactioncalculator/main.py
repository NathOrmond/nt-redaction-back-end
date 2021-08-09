import numpy as np
import pandas as pd

def friendly_table_outputter(array, a, b):
    df = pd.DataFrame(array)
    df=df.set_index([list(a)])
    df=df.set_axis([list(b)], axis=1)
    
#     print(df, '\n')
    return df

def levenschtein_distance_basic(a, b, output_distance=True, output_table=False):
    a = ' '+a # a_0 is always the empty string
    b = ' '+b
    
    # costing
    deletion_cost = 1
    insertion_cost = 1
    
    D = np.zeros((len(a), len(b)), dtype=int)
    
    for i in range(len(a)):
        D[i][0] = i
    
    for j in range(len(b)):
        D[0][j] = j
        
    for j in range(1, len(b)):
        for i in range(1, len(a)):
            if a[i] == b[j]:
                substitution_cost = 0
            else:
                substitution_cost = 1
            
            D[i, j] = min(                          # can probably change what is counted as a change by creating a subfunction of this and tweaking it
                D[i-1, j] + deletion_cost,
                D[i, j-1] + insertion_cost, 
                D[i-1, j-1] + substitution_cost
            )
            
    if output_table:
        return friendly_table_outputter(D, a, b)
    if output_distance:
        return D[-1][-1]

def get_distances(func, sources, targets=[]):
    '''
    Returns a dataframe with the distances from the sources to the targets. 
    If the targets is empty it returns the distance between all elements of the sources to each other
    
    Inputs
    
    func:       the distance calculator function to use
    sources:    list of strings
    targets:    empty list or list of strings
    
    Outputs:
    pd.DataFrame object with rows = sources and columns = targets.
    '''
    if targets == []:
        targets=sources
        
    df = pd.DataFrame( index = sources, columns = targets )
    
    for i in targets:
        for j in sources:
            df[i][j] = func(i, j)
    
    return df

if __name__=="__main__":
    print(levenschtein_distance_basic('kitten', 'sitting', output_distance=False, output_table=True))
    
