from Reader import Reader
import datetime

class ReaderConcret(Reader):

    def __init__ (self):
        Reader.__init__(self)
        self.firstRow.append ("day_of_week")
        self.firstRow.append("hour")
        self.firstRow.append("min")
        pass

    def read (self, row ):
        self.rowList = []
        dateFormat = self.getDateFormatted(row[2])
        self.rowList.append(int(dateFormat.weekday())+1)
        self.rowList.append(dateFormat.hour)
        self.rowList.append(dateFormat.minute)
        return self.rowList

    def getDateFormatted (self , date):
        year = int(date.split('-')[0])
        month = int(date.split('-')[1])
        day = int(date.split('-')[2].split('T')[0])
        time = date.split('T')[1]
        hour = int(time.split(':')[0])
        min = int(time.split(':')[1])
        dateFormat = datetime.datetime(year, month , day , hour , min)
        return dateFormat

