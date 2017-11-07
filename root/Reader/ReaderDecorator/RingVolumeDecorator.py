from ReaderDecoratorAbs import ReaderDecoratorAbs


class RingVolumeDecorator(ReaderDecoratorAbs):
    def __init__(self, reader):
        self.ringVolume = 0
        reader.get_firstRow().append("ring_volumen")
        ReaderDecoratorAbs.__init__(self, reader)

    def read(self, row):
        list = self.reader.read(row)
        if "audio" in row[3]:
            if "volume" in row[3]:
                if "ring" in row[3]:
                    self.ringVolume = row[4]
        list.append(self.ringVolume)
        return list