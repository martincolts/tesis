from ReaderDecoratorAbs import ReaderDecoratorAbs


class WifiDecorator(ReaderDecoratorAbs):
    def __init__(self, reader):
        list = reader.get_firstRow()
        list.append("wifi")
        ReaderDecoratorAbs.__init__(self, reader)
        self.wifiStatus = 1

    def read(self, row):
        list = self.reader.read(row)
        if "wifi" in row[3]:
            if "state" in row[3]:
                if "enabled" in row[4]:
                    self.wifiStatus = 1
                elif "disabled" in row[4]:
                    self.wifiStatus = 0
        list.append(self.wifiStatus)
        return list

    def get_wifiPowerStatus(self):
        return self.wifiStatus
