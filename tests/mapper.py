import os
from redactioncalculator.mapper import mapper, file_to_wordlist, unmapper

if __name__=="__main__":
    wordlist=file_to_wordlist(os.getcwd()+'/tests/a_sentence.txt')
    mapped_text, mapping_dict=mapper(wordlist)
    unmapped=unmapper(mapping_dict, mapped_text)
    print(mapped_text)
    print(unmapped)
    print(wordlist==unmapped)