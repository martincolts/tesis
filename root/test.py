import csv
from Reader.ReaderConcret import ReaderConcret
from Reader.ReaderDecorator.BateryDecorator import BateryDecorator
from Reader.ReaderDecorator.WifiDecorator import WifiDecorator
from Reader.ReaderDecorator.BluetoothStateDecorator import BluetoothStateDecorator
from Reader.ReaderDecorator.MobileConnStateDecorator import MobileConnStateDecorator

filePath = '00f1221ebf94129c8d4643d1542ebd4c1fabf9d5.csv'
count = 0
reader = ReaderConcret ()
reader = BateryDecorator (reader, filePath ,count)
reader = WifiDecorator (reader)
reader = BluetoothStateDecorator (reader)
reader = MobileConnStateDecorator (reader)

with open (filePath , 'rb' )as inFile:
    with open ('result.csv','wb') as outFile:
        readFile = csv.reader (inFile , delimiter=';', quotechar='|')
        writeFile = csv.writer (outFile , delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writeFile.writerow(reader.get_firstRow())
        for row in readFile:
            if count < readFile.line_num:
                writeFile.writerow(reader.read(row))

import fileinput
seen = set() # set for fast O(1) amortized lookup
for line in fileinput.FileInput('result.csv', inplace=1):
    if line in seen: continue # skip duplicate

    seen.add(line)
    print line, # standard output is now redirected to the file