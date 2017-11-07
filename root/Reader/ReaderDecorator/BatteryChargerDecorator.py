from ReaderDecoratorAbs import ReaderDecoratorAbs


class BatteryChargerDecorator(ReaderDecoratorAbs):
    def __init__(self, reader):
        self.batteryCharger = 0
        reader.get_firstRow().append("battery_charger")
        ReaderDecoratorAbs.__init__(self, reader)

    def read(self, row):
        list = self.reader.read(row)
        if "power|charger" in row[3]:
            if "disconnected" in row[4]:
                self.batteryCharger = 0
            elif "ac" in row[4]:
                self.batteryCharger = 1
            elif "usb" in row[4]:
                self.batteryCharger = 2
        list.append(self.batteryCharger)
        return list