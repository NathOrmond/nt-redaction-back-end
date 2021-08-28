import os
from redactioncalculator.mapper import mapper, text_to_wordlist

if __name__=="__main__":
    wordlist=text_to_wordlist(os.getcwd()+'/tests/a_sentence.txt')
    print(mapper(wordlist))