from abc import ABCMeta , abstractmethod
class Reader(object):
    __metaclass__ = ABCMeta

    def __init__(self ):
        self.rowList = []
        self.firstRow = []
        pass

    def get_firstRow (self):
        return self.firstRow

    @abstractmethod
    def read (self , row ):
        pass