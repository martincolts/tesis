from ReaderDecoratorAbs import ReaderDecoratorAbs


class ScreenModeDecorator(ReaderDecoratorAbs):
    def __init__(self, reader):
        self.screenMode = 0
        reader.get_firstRow().append("screen_automatic_mode")
        ReaderDecoratorAbs.__init__(self, reader)

    def read(self, row):
        list = self.reader.read(row)
        if "screen|brightness|mode" in row[3]:
            if "manual" in row[4]:
                self.screenMode = 0
            elif "automatic" in row[4]:
                self.screenMode = 1
        list.append(self.screenMode)
        return list