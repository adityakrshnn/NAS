import datetime

if __name__ == '__main__':
    dateFrom = datetime.date(1990,1,1)
    dateTo = datetime.date(1999,12,31)
    d = dateTo - dateFrom
    days = d.days
    weeks = days//7
    extraDays = days%7
    #print(weeks)
    #print(extraDays)
    day1 = dateFrom.weekday()
    #print(day1)
    day2 = dateTo.weekday()
    #Monday is 0 and sunday is 6
    #For thursday
    if((day1+(extraDays))%6>=3):
        print("Number of Thurdays is: "+str(weeks+1))
    else:
        print("Number of Thurdays is: " + str(weeks))