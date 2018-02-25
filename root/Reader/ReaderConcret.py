from Reader import Reader
import datetime

class ReaderConcret(Reader):

    def __init__ (self):
        Reader.__init__(self)
        self.firstRow.append ("monday")
        self.firstRow.append("tuesday")
        self.firstRow.append("wednesday")
        self.firstRow.append("thursday")
        self.firstRow.append("friday")
        self.firstRow.append("saturday")
        self.firstRow.append("sunday")
        self.firstRow.append("hour")
        self.firstRow.append("min")
        self.firstRow.append("date")
        pass

    def read (self, row ):
        self.rowList = []
        dateFormat = self.getDateFormatted(row[2])
        day = int(dateFormat.weekday())+1
        if day == 1:
            self.rowList.append(1)
            self.rowList.append(0)
            self.rowList.append(0)
            self.rowList.append(0)
            self.rowList.append(0)
            self.rowList.append(0)
            self.rowList.append(0)
        elif day == 2:
            self.rowList.append(0)
            self.rowList.append(1)
            self.rowList.append(0)
            self.rowList.append(0)
            self.rowList.append(0)
            self.rowList.append(0)
            self.rowList.append(0)
        elif day == 3:
            self.rowList.append(0)
            self.rowList.append(0)
            self.rowList.append(1)
            self.rowList.append(0)
            self.rowList.append(0)
            self.rowList.append(0)
            self.rowList.append(0)
        elif day == 4:
            self.rowList.append(0)
            self.rowList.append(0)
            self.rowList.append(0)
            self.rowList.append(1)
            self.rowList.append(0)
            self.rowList.append(0)
            self.rowList.append(0)
        elif day == 5:
            self.rowList.append(0)
            self.rowList.append(0)
            self.rowList.append(0)
            self.rowList.append(0)
            self.rowList.append(1)
            self.rowList.append(0)
            self.rowList.append(0)
        elif day == 6:
            self.rowList.append(0)
            self.rowList.append(0)
            self.rowList.append(0)
            self.rowList.append(0)
            self.rowList.append(0)
            self.rowList.append(1)
            self.rowList.append(0)
        else:
            self.rowList.append(0)
            self.rowList.append(0)
            self.rowList.append(0)
            self.rowList.append(0)
            self.rowList.append(0)
            self.rowList.append(0)
            self.rowList.append(1)
        self.rowList.append(dateFormat.hour)
        self.rowList.append(dateFormat.minute)
        self.rowList.append(row[2])
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

