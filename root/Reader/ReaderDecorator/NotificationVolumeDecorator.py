from ReaderDecoratorAbs import ReaderDecoratorAbs


class NotificationVolumeDecorator(ReaderDecoratorAbs):
    def __init__(self, reader):
        self.notificationVolume = 0
        reader.get_firstRow().append("notificadion_volumen")
        ReaderDecoratorAbs.__init__(self, reader)

    def read(self, row):
        list = self.reader.read(row)
        if "audio" in row[3]:
            if "volume" in row[3]:
                if "notification" in row[3]:
                    self.notificationVolume = row[4]
        list.append(self.notificationVolume)
        return list