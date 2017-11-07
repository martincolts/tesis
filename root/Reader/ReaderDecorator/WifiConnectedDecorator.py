from ReaderDecoratorAbs import ReaderDecoratorAbs


class WifiConnectedDecorator(ReaderDecoratorAbs):
    def __init__(self, reader):
        self.wifiConnected = 0
        reader.get_firstRow().append("wifi_connected")
        ReaderDecoratorAbs.__init__(self, reader)

    def read(self, row):
        list = self.reader.read(row)
        if "wifi" in row[3]:
            if "connected" in row[3]:
                self.wifiConnected = 1
            elif "scan" in row[3]:
                self.wifiConnected = 0
        if self.get_wifiConnectedStatus() == 0:
            self.wifiConnected = 0
        list.append(self.wifiConnected)
        return list

    def get_wifiConnectedStatus(self):
        return self.wifiConnected
