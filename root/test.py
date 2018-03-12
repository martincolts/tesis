import csv
from Reader.ReaderConcret import ReaderConcret
from Reader.ReaderDecorator.BateryDecorator import BateryDecorator
from Reader.ReaderDecorator.WifiDecorator import WifiDecorator
from Reader.ReaderDecorator.BluetoothStateDecorator import BluetoothStateDecorator
from Reader.ReaderDecorator.MobileConnStateDecorator import MobileConnStateDecorator
from Reader.ReaderDecorator.WifiConnectedDecorator import WifiConnectedDecorator
from Reader.ReaderDecorator.WifiOnButNotConnectedDecorator import WifiOnButNotConnectedDecorator
from Reader.ReaderDecorator.BluetoothDiscoveryDecorator import BluetoothDiscoveryDecorator
from Reader.ReaderDecorator.AirplaneDecorator import AirplaneDecorator
from Reader.ReaderDecorator.SystemVolumeDecorator import SystemVolumeDecorator
from Reader.ReaderDecorator.DtmfVolumeDecorator import DtmfVolumeDecorator
from Reader.ReaderDecorator.MusicVolumeDecorator import MusicVolumeDecorator
from Reader.ReaderDecorator.NotificationVolumeDecorator import NotificationVolumeDecorator
from Reader.ReaderDecorator.RingermodeDecorator import RingermodeDecorator
from Reader.ReaderDecorator.BatteryTempDecorator import BatteryTempDecorator
from Reader.ReaderDecorator.BatteryVoltageDecorator import BatteryVoltageDecorator
from Reader.ReaderDecorator.BatteryChargerDecorator import BatteryChargerDecorator
from Reader.ReaderDecorator.ScreenBrightnessDecorator import ScreenBrightnessDecorator
from Reader.ReaderDecorator.ScreenModeDecorator import ScreenModeDecorator
from Reader.ReaderDecorator.ScreenPowerDecorator import ScreenPowerDecorator
from Reader.ReaderDecorator.CPUDecorator import CPUDecorator
from Reader.ReaderDecorator.MemoryFreeDecorator import MemoryFreeDecorator

filePath = '0269e21475ac65ad57fbec9c83ab4960ec66581b.csv'
count = 0
reader = ReaderConcret()
reader = BateryDecorator(reader, filePath, count)
reader = WifiDecorator(reader)
reader = BluetoothStateDecorator(reader)
reader = MobileConnStateDecorator(reader)
reader = WifiConnectedDecorator(reader)
reader = WifiOnButNotConnectedDecorator(reader)
reader = BluetoothDiscoveryDecorator(reader)
reader = AirplaneDecorator(reader)
reader = SystemVolumeDecorator(reader)
reader = DtmfVolumeDecorator(reader)
reader = MusicVolumeDecorator(reader)
reader = NotificationVolumeDecorator(reader)
reader = RingermodeDecorator(reader)# normal=0, silent=1, vibrate=2
reader = BatteryTempDecorator(reader)
reader = BatteryVoltageDecorator(reader)
reader = BatteryChargerDecorator(reader)
reader = ScreenBrightnessDecorator(reader)
reader = ScreenModeDecorator(reader)# manual=0, automatic=1
reader = ScreenPowerDecorator(reader)# off=0, on=1
reader = CPUDecorator(reader)
reader = MemoryFreeDecorator(reader)

saveType = "24PerDay"
import sys

with open(filePath, 'rb')as inFile:
    with open('file2_24PerDay.csv', 'wb') as outFile:
        readFile = csv.reader(inFile, delimiter=';', quotechar='|')
        writeFile = csv.writer(outFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writeFile.writerow(reader.get_firstRow())
        hour = 0
        min20 = 0
        min40 = 0
        min00 = 0
        if saveType == "24PerDay":
            index=0
            for row in readFile:
                index=index+1
                line = reader.read(row)
                if line[7]!=hour:
                    hour = line[7]
                    writeFile.writerow(line)
                sys.stdout.write("Progress: %d%%   \r" % (index*100/170204505) )
                sys.stdout.flush()
        elif saveType == "3PerHour":
            for row in readFile:
                line = reader.read(row)
                if line[7] == hour:
                    if min20 == 0:
                        if line[8]>=15 and line[8]<=25:
                            min20=1
                            writeFile.writerow(line)
                    if min40 == 0:
                        if line[8]>=35 and line[8]<=45:
                            min40=1
                            writeFile.writerow(line)
                    if min00 == 0:
                        if line[8]>=50 and line[8]<=59:
                            min00=1
                            writeFile.writerow(line)
                else:
                    hour = line[7]
                    min00=0
                    min20=0
                    min40=0
        else:
            index =0
            for row in readFile:
                index = index+1
                line = reader.read(row)
                if index%25 == 0:
                    if count < readFile.line_num:
                        writeFile.writerow(line)
                sys.stdout.write("Progress: %d%%   \r" % (index/12121) )
                sys.stdout.flush()

#import fileinput

#seen = set()  # set for fast O(1) amortized lookup
#for line in fileinput.FileInput('result.csv', inplace=1):
#    if any(line) in seen: continue  # skip duplicate

#    seen.add(line)
#    print line  # standard output is now redirected to the file

#input = open('result.csv', 'rb')
#output = open('result2.csv', 'wb')
#writer = csv.writer(output)
#for row in csv.reader(input):
#    if any(row):
#        writer.writerow(row)
#input.close()
#output.close()
