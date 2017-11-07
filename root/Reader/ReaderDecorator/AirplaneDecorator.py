from ReaderDecoratorAbs import ReaderDecoratorAbs


class AirplaneDecorator(ReaderDecoratorAbs):
    def __init__(self, reader):
        reader.get_firstRow().append("airplane_on_off")
        self.airplaneOn = 0
        ReaderDecoratorAbs.__init__(self, reader)

    def read(self, row):
        list = self.reader.read(row)
        if "airplane" in row[3]:
            if "on" in row[3]:
                self.airplaneOn = 1
            elif "off" in row[3]:
                self.airplaneOn = 0
        list.append(self.airplaneOn)
        return list
