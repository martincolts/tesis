from Reader import Reader

class ReaderConcret(Reader):

    def __init__ (self):
        Reader.__init__(self)
        pass

    def read (self, row ):
        self.rowList = []
        self.rowList.append(row[0])
        self.rowList.append(row[2])
        return self.rowList
