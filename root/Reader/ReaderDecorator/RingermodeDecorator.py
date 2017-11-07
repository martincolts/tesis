from ReaderDecoratorAbs import ReaderDecoratorAbs


class RingermodeDecorator(ReaderDecoratorAbs):
    def __init__(self, reader):
        self.ringermode = 0
        reader.get_firstRow().append("ringermode")
        ReaderDecoratorAbs.__init__(self, reader)

    def read(self, row):
        list = self.reader.read(row)
        if "ringermode" in row[3]:
            if "normal" in row[4]:
                self.ringermode = 0
            elif "silent" in row [4]:
                self.ringermode = 1
            elif "vibrate" in row [4]:
                self.ringermode = 2
        list.append(self.ringermode)
        return list