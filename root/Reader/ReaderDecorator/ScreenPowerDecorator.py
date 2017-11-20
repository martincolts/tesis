from ReaderDecoratorAbs import ReaderDecoratorAbs


class ScreenPowerDecorator(ReaderDecoratorAbs):
    def __init__(self, reader):
        self.screenPower = 0
        reader.get_firstRow().append("screen_on")
        ReaderDecoratorAbs.__init__(self, reader)

    def read(self, row):
        list = self.reader.read(row)
        if "screen|power" in row[3]:
            if "off" in row[4]:
                self.screenPower = 0
            elif "on" in row[4]:
                self.screenPower = 1
        list.append(self.screenPower)
        return list