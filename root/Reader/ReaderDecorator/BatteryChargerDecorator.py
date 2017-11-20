from ReaderDecoratorAbs import ReaderDecoratorAbs


class BatteryChargerDecorator(ReaderDecoratorAbs):
    def __init__(self, reader):
        self.disconected = 1
        self.ac = 0
        self.usb = 0
        reader.get_firstRow().append("disconected")
        reader.get_firstRow().append("ac")
        reader.get_firstRow().append("usb")
        ReaderDecoratorAbs.__init__(self, reader)

    def read(self, row):
        list = self.reader.read(row)
        if "power|charger" in row[3]:
            if "disconnected" in row[4]:
                self.disconected = 1
                self.usb = 0
                self.ac = 0
            elif "ac" in row[4]:
                self.ac= 1
                self.disconected = 0
                self.usb = 0
            elif "usb" in row[4]:
                self.usb = 1
                self.disconected = 0
                self.ac =0
        list.append(self.disconected)
        list.append(self.ac)
        list.append(self.usb)
        return list