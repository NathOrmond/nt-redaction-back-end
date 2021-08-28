from main import levenschtein_distance_basic
import pandas as pd

_default_distance_func=levenschtein_distance_basic

def get_distances(sources, targets=[]):
    '''
    Returns a dataframe with the distances from the sources to the targets. 
    If the targets is empty it returns the distances between all elements of 
    the sources to each other
    
    Inputs
    ------
    sources:    list of strings
    targets:    empty list or list of strings
    
    Output
    ------
    pd.DataFrame object with rows = sources and columns = targets.
    '''
    if targets == []:
        targets=sources
        
    df = pd.DataFrame( index = sources, columns = targets )
    
    for i in targets:
        for j in sources:
            df[i][j] = _default_distance_func(i, j)
    
    return df

if __name__=="__main__":
    sources=['kitten', 'sitting', 'mitten']
    print(get_distances(sources))