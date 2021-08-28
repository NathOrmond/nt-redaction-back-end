from redactioncalculator.distance import get_distances, get_distances_from_filepaths

if __name__=="__main__":
    print('\n')
    print('Testing get_distances...')
    print('Input:')
    sources=['kitten', 'sitting', 'mitten']
    print('sources:', sources)
    print('Output:')
    print(get_distances(sources))
    print('\n')

    print('Testing get_distances_from_filepaths...')
    files={'a_sentence':'/tests/a_sentence.txt', 'with_dupes':'/tests/with_dupes.txt'}
    print('Input:', files)
    print('Output:')
    print(get_distances_from_filepaths(files))
    print('\n')