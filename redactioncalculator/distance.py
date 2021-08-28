from .variations import levenschtein_distance_basic
from .mapper import file_to_wordlist, mapper
import pandas as pd
import os

_default_distance_func=levenschtein_distance_basic

def get_distances_from_filepaths(files):
    '''
    A wrapper for get_distances that allows passing filepaths directly.

    Input
    -----
    files   dict    A dictionary with of the form {name: filepath}

    Ouput
    -----
    pd.DataFrame with the distances from all files to each other.
    '''
    sources=[]
    mapping_dict={} # mapping dictionary must be the same for the files to be comparable

    for filename in files.keys():
        path=files[filename]
        if not os.path.exists(path):
            path=os.getcwd()+path
            if not os.path.exists(path):
                raise RuntimeError('Filepath '+path+' does not exist.')

        wordlist=file_to_wordlist(path)
        mapped_text, mapping_dict=mapper(wordlist, mapping_dict)
        #sources.append(mapped_text)
        files[filename]=mapped_text
    
    distances=get_distances([mapped_text for filename, mapped_text in files.items()])
    rev_files={y: x for x, y in files.items()}
    return distances.rename(columns=rev_files, index=rev_files)

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