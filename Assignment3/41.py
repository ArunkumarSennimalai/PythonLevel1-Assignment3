import calendar

class CalendarOperations:
    def displayOneYearCalendar(self,year):
        print calendar.calendar(year,c=10)
    
    def leapdaysCount(self,startyear,endyear):
        return calendar.leapdays(startyear,endyear)
    
    def isLeapYear(self,year):
        return calendar.isleap(year)
    
    def displayOneMonthCalendar(self,month,year=2016):
        print calendar.month(2016,month)

if __name__ == "__main__":
    try:
        c1 = CalendarOperations()
        #1year calendar
        c1.displayOneYearCalendar(2016)
        #leapdays count
        no_of_leapdays = c1.leapdaysCount(1980,2025)
        print "Leap days between 1980 to 2025 is",no_of_leapdays
        #check leap year or not
        year = input("Enter the year to check leap year or not")
        print c1.isLeapYear(year)
        #1month calendar
        month  = input("Enter the month which is needed to be displayed")
        c1.displayOneMonthCalendar(month)
        
    except Exception as e:
        print e
