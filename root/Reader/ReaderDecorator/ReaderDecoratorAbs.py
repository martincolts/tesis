from ..Reader import Reader
from abc import ABCMeta, abstractmethod


class ReaderDecoratorAbs(Reader):
    __metaclass__ = ABCMeta

    def __init__(self, reader):
        self.reader = reader

    def get_firstRow(self):
        return self.reader.get_firstRow()

    def get_wifiPowerStatus(self):
        return self.reader.get_wifiPowerStatus()

    def get_wifiConnectedStatus(self):
        return self.reader.get_wifiConnectedStatus()
