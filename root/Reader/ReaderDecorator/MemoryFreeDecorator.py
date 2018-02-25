from ReaderDecoratorAbs import ReaderDecoratorAbs
class MemoryFreeDecorator(ReaderDecoratorAbs):

    def __init__(self , reader):
        reader.get_firstRow().append("mem_free")
        self.memFree = 0
        ReaderDecoratorAbs.__init__(self , reader)

    def read(self , row ):
        list = self.reader.read(row)
        if "system" in row[3]:
            if "memory" in row[3]:
                if "free" in row[3]:
                    self.memFree = row[4].split(" ")[0]
        list.append(self.memFree)
        return list