from datetime import datetime
import random
import string

class Mapper():
    '''This class will map every unique word in a file to a randomly
    assigned unique id.'''
    
    def __init__(self, in_dir):
        self.in_dir=in_dir    # don't want to be able to modify this
        self._words={} 
        self._mapped_text = self.text_mapper()
        
    @property
    def mapped_text(self):
        return self._mapped_text
    
    def _text_to_wordlist(self, in_dir):
        '''Reads file from in_dir and returns a list with all words in order, 
        including duplicates.'''
        words = []
        with open(in_dir) as file:
            for line in file:
                line=line.strip()
                for word in line.split(' '):
                    words.append(word)
        return words
    
    def _word_id(self, word):
        '''
        Gets a word id for every unique word if it is not already present in 
        _words. Once assigned it is also saved in _words.
        '''
        if word not in self._words.keys():
            # this method of getting ids can encode 218340106 million words (english has 1 million)
            lst = [random.choice(string.ascii_letters + string.digits) for n in range(8)]
            s = "".join(lst)
            word_id='word_'+s
            self._words[word]=word_id
        return self._words[word]
    
    def text_mapper(self):
        '''
        Maps a text file to a string replacing words with their unique ids.
        '''
        wordlist=self._text_to_wordlist(self.in_dir)
        mapped_wordlist=[]
        for word in wordlist:
            mapped_word=self._word_id(word)
            mapped_wordlist.append(mapped_word)
        return ' '.join(mapped_wordlist)
    
if __name__=='__main__':
    f=Mapper("../tests/a_sentence.txt")
    print(f.mapped_text)