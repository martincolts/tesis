from ReaderDecoratorAbs import ReaderDecoratorAbs


class ScreenBrightnessDecorator(ReaderDecoratorAbs):
    def __init__(self, reader):
        self.screenBrig = 0
        reader.get_firstRow().append("screen_brightness")
        ReaderDecoratorAbs.__init__(self, reader)

    def read(self, row):
        list = self.reader.read(row)
        if "screen" in row[3]:
            if "brightness" in row [3]:
                if "level" in row[3]:
                    self.screenBrig= row[4]
        list.append(self.screenBrig)
        return list