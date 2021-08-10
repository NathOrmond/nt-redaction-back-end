import os
from datetime import datetime
import pytz

class OutputManager():
    _default_dir=os.getcwd()+'/output/'+datetime.now(pytz.timezone('Europe/London')).strftime('%Y-%m-%d')+'/'
    
    def __init__(self, dir=None):
        self._dir=dir
        return None
    
    @property
    def dir(self):
        if self._dir is None:
            self._dir=self._default_dir
        return self._dir
    
    @dir.setter
    def dir(self, out_dir):
        self._dir=dir
    
    def filename(self, s=''):
        return datetime.now(pytz.timezone('Europe/London')).strftime('%Y-%m-%d %H:%M:%S')+' '+s