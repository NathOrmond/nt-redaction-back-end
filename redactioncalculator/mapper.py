import string
import random

def file_to_wordlist(in_dir):
    '''
    Reads file from in_dir and returns a list with all words in order, 
    including duplicates.
    '''
    words = []
    with open(in_dir) as file:
        for line in file:
            line=line.strip()
            for word in line.split(' '):
                words.append(word)
    return words

def mapper(wordlist, dictionary={}):
    '''
    Returns a string with the words from wordlist mapped to unique characters.
    
    Inputs
    ------
    wordlist:    lst    A list of words.
    dictionary:  dict   A dictionary mapping words to characters, to be used if multiple
                        wordlists need to be encoded using the same mapping.
    
    Returns
    -------
    str, dict           A string containing the mapped words as characters and a dictionary
                        containing the mapping.
    
    Raises
    ------
    RuntimeError: if there aren't enough carracters to encode the wordlist.
    '''
    out=''
    chars=string.ascii_letters+string.digits
    wordlist=[word.lower() for word in wordlist]
    dictionary=dictionary # flushes any previous local dictionaries
    
    if len(wordlist) > len(chars):
        raise RuntimeError('The wordlist is too long and cannot be encoded by characters only.')
    
    for word in wordlist:
        if word not in dictionary.keys():
            c=random.choice(chars)
            chars=chars.replace(c, "") #ensuring mapping uniqueness
            dictionary[word]=c
        out+=dictionary[word]
    return out, dictionary

def unmapper(mapping_dict, mapped_text):
    out=[]
    mapping_dict={y:x for x,y in mapping_dict.items()} # switching keys and items
    for char in mapped_text:
        out.append(mapping_dict[char])
    return out