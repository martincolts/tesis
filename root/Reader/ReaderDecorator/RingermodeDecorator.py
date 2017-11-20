from ReaderDecoratorAbs import ReaderDecoratorAbs


class RingermodeDecorator(ReaderDecoratorAbs):
    def __init__(self, reader):
        self.normal = 1
        self.silent = 0
        self.vibrate = 0
        reader.get_firstRow().append("ringermode_normal")
        reader.get_firstRow().append("ringermode_silent")
        reader.get_firstRow().append("ringermode_vibrate")
        ReaderDecoratorAbs.__init__(self, reader)

    def read(self, row):
        list = self.reader.read(row)
        if "ringermode" in row[3]:
            if "normal" in row[4]:
                self.normal = 1
                self.silent = 0
                self.vibrate = 0
            elif "silent" in row [4]:
                self.normal = 0
                self.vibrate = 0
                self.silent = 1
            elif "vibrate" in row [4]:
                self.vibrate = 1
                self.normal = 0
                self.silent = 0
        list.append(self.normal)
        list.append(self.silent)
        list.append(self.vibrate)
        return list