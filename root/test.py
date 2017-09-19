import csv
from Reader.ReaderConcret import ReaderConcret
from Reader.ReaderDecorator.BateryDecorator import BateryDecorator
from Reader.ReaderDecorator.WifiDecorator import WifiDecorator
from Reader.ReaderDecorator.BluetoothStateDecorator import BluetoothStateDecorator
from Reader.ReaderDecorator.MobileConnStateDecorator import MobileConnStateDecorator

filePath = 'in.csv'
count = 0
reader = ReaderConcret ()
reader = BateryDecorator (reader, filePath ,count)
reader = WifiDecorator (reader)
reader = BluetoothStateDecorator (reader)
reader = MobileConnStateDecorator (reader)

with open (filePath , 'rb' )as inFile:
    with open ('result.csv','wb') as outFile:
        readFile = csv.reader (inFile , delimiter=';', quotechar='|')
        writeFile = csv.writer (outFile , delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in readFile:
            if count < readFile.line_num:
                writeFile.writerow(reader.read(row))

