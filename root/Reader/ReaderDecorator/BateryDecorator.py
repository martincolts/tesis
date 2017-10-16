from ReaderDecoratorAbs import ReaderDecoratorAbs
import csv
class BateryDecorator(ReaderDecoratorAbs):

    def __init__(self , reader , filePath , count):
        reader.firstRow.append("battery")
        count = 0
        with open(filePath, 'rb')as inFile:
            readFile = csv.reader(inFile, delimiter=';', quotechar='|')
            for row in readFile:
                count=count+1
                if "power" in row[3]:
                    if "level" in row[3]:
                        if row[4] != '0':
                            self.bateryLevel=row[4]
                            break
        ReaderDecoratorAbs.__init__(self , reader)

    def read(self , row ):
        list = self.reader.read(row)
        if "power" in row[3]:
            if "level" in row[3]:
                self.bateryLevel = row[4]
        list.append(self.bateryLevel)
        return list
