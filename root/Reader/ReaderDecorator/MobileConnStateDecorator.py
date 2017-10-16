from ReaderDecoratorAbs import ReaderDecoratorAbs
class MobileConnStateDecorator(ReaderDecoratorAbs):

    def __init__(self , reader):
        self.mobileState = 0
        reader.get_firstRow().append("data")
        ReaderDecoratorAbs.__init__(self , reader)


    def read(self , row ):
        list = self.reader.read(row)
        if "conn" in row[3]:
            if "mobile" in row[3]:
                if "detailedstate" in row[3]:
                    if "CONNECTED" in row[4]:
                        self.mobileState=1
                    if "DISCONNECTED" in row[4]:
                        self.mobileState=0
        list.append(self.mobileState)
        return list