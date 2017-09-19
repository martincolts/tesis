from ReaderDecoratorAbs import ReaderDecoratorAbs
class BluetoothStateDecorator(ReaderDecoratorAbs):

    def __init__(self , reader):
        ReaderDecoratorAbs.__init__(self , reader)
        self.bluetoothStatus = 0

    def read(self , row ):
        list = self.reader.read(row)
        if "bluetooth" in row[3]:
            if "state" in row[3]:
                if "turning on" in row[4]:
                    self.bluetoothStatus = 1
                if "turning off" in row[4]:
                    self.bluetoothStatus = 0
        list.append(self.bluetoothStatus)
        return list