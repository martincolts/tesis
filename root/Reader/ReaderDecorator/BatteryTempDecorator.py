from ReaderDecoratorAbs import ReaderDecoratorAbs


class BatteryTempDecorator(ReaderDecoratorAbs):
    def __init__(self, reader):
        self.batteryTemp = 0
        reader.get_firstRow().append("battery_temp")
        ReaderDecoratorAbs.__init__(self, reader)

    def read(self, row):
        list = self.reader.read(row)
        if "power|battery|temperature" in row[3]:
            self.batteryTemp = row[4]
        list.append(self.batteryTemp)
        return list