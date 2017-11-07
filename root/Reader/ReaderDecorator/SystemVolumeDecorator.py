from ReaderDecoratorAbs import ReaderDecoratorAbs


class SystemVolumeDecorator(ReaderDecoratorAbs):
    def __init__(self, reader):
        self.systemVolume = 0
        reader.get_firstRow().append("system_volumen")
        ReaderDecoratorAbs.__init__(self, reader)

    def read(self, row):
        list = self.reader.read(row)
        if "audio" in row[3]:
            if "volume" in row[3]:
                if "system" in row[3]:
                    self.systemVolume = row[4]
        list.append(self.systemVolume)
        return list