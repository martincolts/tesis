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

filePath = 'in.csv'
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

with open(filePath, 'rb')as inFile:
    with open('result.csv', 'wb') as outFile:
        readFile = csv.reader(inFile, delimiter=';', quotechar='|')
        writeFile = csv.writer(outFile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writeFile.writerow(reader.get_firstRow())
        for row in readFile:
            if count < readFile.line_num:
                writeFile.writerow(reader.read(row))

import fileinput

seen = set()  # set for fast O(1) amortized lookup
for line in fileinput.FileInput('result.csv', inplace=1):
    if line in seen: continue  # skip duplicate

    seen.add(line)
    print line,  # standard output is now redirected to the file
