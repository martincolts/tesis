from ..Reader import Reader
from abc import ABCMeta , abstractmethod
class ReaderDecoratorAbs(Reader):

    __metaclass__ = ABCMeta

    def __init__ (sefl , reader):
        sefl.reader = reader

    def get_firstRow(self):
        return self.reader.get_firstRow()
