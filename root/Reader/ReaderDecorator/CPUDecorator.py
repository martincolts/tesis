from ReaderDecoratorAbs import ReaderDecoratorAbs
class CPUDecorator(ReaderDecoratorAbs):

    def __init__(self , reader):
        reader.get_firstRow().append("cores")
        reader.get_firstRow().append("maxfreq")
        reader.get_firstRow().append("minfreq")
        self.cores = 0
        self.maxfreq = 0
        self.minfreq = 0
        ReaderDecoratorAbs.__init__(self , reader)

    def read(self , row ):
        list = self.reader.read(row)
        if "system" in row[3]:
            if "cpu" in row[3]:
                if "cores" in row[3]:
                    self.cores = row[4]
                if "maxfreq" in row[3]:
                    self.maxfreq = row[4]
                if "minfreq" in row[3]:
                    self.minfreq = row[4]
        list.append(self.cores)
        list.append(self.maxfreq)
        list.append(self.minfreq)
        return list