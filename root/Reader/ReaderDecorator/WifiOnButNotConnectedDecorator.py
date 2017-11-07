from ReaderDecoratorAbs import ReaderDecoratorAbs


class WifiOnButNotConnectedDecorator(ReaderDecoratorAbs):
    def __init__(self, reader):
        list = reader.get_firstRow().append("wifi_scanning")
        self.wifiScanning = 1
        ReaderDecoratorAbs.__init__(self, reader)

    def read(self, row):
        list = self.reader.read(row)
        wifiStatus = self.get_wifiPowerStatus()
        wifiConnected = self.get_wifiConnectedStatus()
        if wifiStatus == 1:
            if wifiConnected == 0:
                self.wifiScanning = 1
            else:
                self.wifiScanning = 0
        else:
            self.wifiScanning = 0
        list.append(self.wifiScanning)
        return list
