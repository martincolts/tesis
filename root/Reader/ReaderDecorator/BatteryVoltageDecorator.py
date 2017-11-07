from ReaderDecoratorAbs import ReaderDecoratorAbs


class BatteryVoltageDecorator(ReaderDecoratorAbs):
    def __init__(self, reader):
        self.batteryvoltage = 0
        reader.get_firstRow().append("battery_volt")
        ReaderDecoratorAbs.__init__(self, reader)

    def read(self, row):
        list = self.reader.read(row)
        if "power|battery|voltage" in row[3]:
            self.batteryvoltage = row[4]
        list.append(self.batteryvoltage)
        return list