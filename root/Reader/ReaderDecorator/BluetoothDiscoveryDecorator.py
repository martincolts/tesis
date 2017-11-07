from ReaderDecoratorAbs import ReaderDecoratorAbs
class BluetoothDiscoveryDecorator(ReaderDecoratorAbs):

    def __init__(self, reader):
        reader.get_firstRow().append("bluetoothDiscovery")
        self.bluetoothDiscovering = 0
        ReaderDecoratorAbs.__init__(self, reader)

    def read(self, row):
        list = self.reader.read(row)
        if "bluetooth" in row[3]:
            if "discovery" in row[3]:
                if "started" in row[4]:
                    self.bluetoothDiscovering = 1
                if "finished" in row[4]:
                    self.bluetoothDiscovering = 0
        list.append(self.bluetoothDiscovering)
        return list
