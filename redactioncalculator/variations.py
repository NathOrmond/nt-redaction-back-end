import numpy as np
from .helpers import friendly_table_outputter

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

if __name__=="__main__":
    print(levenschtein_distance_basic('kitten', 'sitting', output_distance=False, output_table=True))
    
