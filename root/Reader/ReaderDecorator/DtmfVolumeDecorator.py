from ReaderDecoratorAbs import ReaderDecoratorAbs


class DtmfVolumeDecorator(ReaderDecoratorAbs):
    def __init__(self, reader):
        self.dtmlVolume = 0
        reader.get_firstRow().append("dtmf_volumen")
        ReaderDecoratorAbs.__init__(self, reader)

    def read(self, row):
        list = self.reader.read(row)
        if "audio" in row[3]:
            if "volume" in row[3]:
                if "dtmf" in row[3]:
                    self.dtmlVolume = row[4]
        list.append(self.dtmlVolume)
        return list