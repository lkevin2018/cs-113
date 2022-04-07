## problem2.py
## Author: Kevin Joseph
## RUID: 212003391

class Date:
    min_year = 1800
    dow_jan1 = "Wednesday"
    
    def year_is_leap(self):
        '''
        This function returns either True or False if the year of the Date object is a leap year.
        '''
        if self.yyyy % 4 == 0 and self.yyyy % 100 != 0:
            return True
        elif (self.yyyy % 100 == 0) and (self.yyyy % 400 == 0):
            return True
        else:
            return False
    
    def month(self):
        '''
        This function returns the month in integer value of the Date object.
        '''
        return self.mm
    
    def day(self):
        '''
        This function returns the day in integer value of the Date object.
        '''
        return self.dd

    def year(self):
        '''
        This function returns the year in integer value of the Date object.
        '''
        return self.yyyy
    
    def daycount(self):
        '''
        This function returns the amount of days in integer format that have elapsed from January 1, 1800.
        '''
        min_year = 1800
        sum = 0
        sum += self.dd
        fullYears = self.yyyy - min_year
        for i in range(fullYears): 
            testD = Date(yyyy = min_year + i)
            if testD.year_is_leap() == True:
                sum += 366
            else:
                sum += 365
        for i in range(1, self.mm):
            if self.year_is_leap() == True and i == 2:
                sum += 29
            elif i == 2:
                sum += 28
            elif i >= 8 and i % 2 == 0:
                sum += 31
            elif i >= 8 and i % 2 == 1:
                sum += 30
            elif i % 2 == 0:
                sum += 30
            elif i % 2 == 1:
                sum += 31
        return sum

    def day_of_week(self):
        '''
        This functions returns the day in string value of the week of the Date. 
        '''
        dow_jan1 = "Wednesday"
        days = [dow_jan1, "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]
        dayC = self.daycount()
        dowInt = (dayC % 7) - 1
        return days[dowInt]
    
    def __init__(self, mm=1, dd=1, yyyy=1800):
        '''
        This function is the constructor of the Date class. The constructor has three parameters mm, dd, yyyy which are the month, date, and year respectively. This function also checks for the validity of the Date and will raise an Exception if the Date is
        '''
        min_year = 1800
        if yyyy >= min_year:
            self.yyyy = yyyy
            if mm >= 1 and mm <= 12:
                self.mm = mm
                if self.year_is_leap() == True and mm == 2:
                    if dd >= 1 and dd <= 29:
                        self.dd = dd
                    else:
                        raise Exception("Please retry your submission.")
                elif mm == 2:
                    if dd >= 1 and dd <= 28:
                        self.dd = dd
                    else:
                        raise Exception("Please retry your submission.")
                elif mm >= 8 and mm % 2 == 0:
                    if dd >= 1 and dd <= 31:
                        self.dd = dd
                    else:
                        raise Exception("Please retry your submission.")
                elif mm >= 8 and mm % 2 == 1:
                    if dd >= 1 and dd <= 30:
                        self.dd = dd
                    else:
                        raise Exception("Please retry your submission.")
                elif mm % 2 == 0:
                    if dd >= 1 and dd <= 30:
                        self.dd = dd
                    else:
                        raise Exception("Please retry your submission.")
                elif mm % 2 == 1:
                    if dd >= 1 and dd <= 31:
                        self.dd = dd
                    else:
                        raise Exception("Please retry your submission.")
            else:
                raise Exception("Please retry your submission.")
            
        else:
            raise Exception("Please retry your submission.")

    def __str__(self):
        '''
        This function returns a string format of the Date object.
        '''
        mos = ""
        if self.mm == 1:
            mos = "January"
        elif self.mm == 2:
            mos = "February"
        elif self.mm == 3:
            mos = "March"
        elif self.mm == 4:
            mos = "April"
        elif self.mm == 5:
            mos = "May"
        elif self.mm == 6:
            mos = "June"
        elif self.mm == 7:
            mos = "July"
        elif self.mm == 8:
            mos = "August"
        elif self.mm == 9:
            mos = "September"
        elif self.mm == 10:
            mos = "October"
        elif self.mm == 11:
            mos = "November"
        else:
            mos = "December"   
        return mos + " " + str(self.dd) + ", " + str(self.yyyy)

    def __repr__(self):
        '''
        This function returns a representation format of the Date object.
        '''
        return "The date is: " + self.day_of_week() + ", " + self + "."    
        
