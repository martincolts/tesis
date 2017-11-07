from ReaderDecoratorAbs import ReaderDecoratorAbs


class MusicVolumeDecorator(ReaderDecoratorAbs):
    def __init__(self, reader):
        self.musicVolume = 0
        reader.get_firstRow().append("music_volumen")
        ReaderDecoratorAbs.__init__(self, reader)

    def read(self, row):
        list = self.reader.read(row)
        if "audio" in row[3]:
            if "volume" in row[3]:
                if "music" in row[3]:
                    self.musicVolume = row[4]
        list.append(self.musicVolume)
        return list