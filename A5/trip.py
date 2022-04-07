"""
Kevin Joseph
RUID: 212003391
Object-Oriented Programming (Spring 2022)
"""

from date import Date

class Trip (Date):
    def __init__(self, init_destination, init_depdate, init_duration):
        if Type(init_destination) == str:
            if Type(init_depdate) == Date:
                if Type(init_duration) == int and init_duration >= 1:
                    self.__destination = init_destination
                    self.__depdate = init_depdate
                    self.__duration = init_duration
                else:
                    raise TypeError("Duration must be an valid integer")
            else:
                raise TypeError("Departure Date must be a valid Date object.")
        else:
            raise TypeError("Destination must be a string.")
        
    def setDestination(self, newDest):
        if Type(newDest) == str:
            self.__destination = newDest
        else:
            raise TypeError("Destination must be a string.")
    
    def setDeparture(self, newDepdate):
        if Type(newDepdate) == Date:
            self.__depdate = newDepdate
        else:
            raise TypeError("Departure Date must be a valid Date object.")
    
    def setDuration(self, newDuration):
        if Type(newDuration) == int and newDuration >= 1:
            self.__duration = newDuration
        else:
            raise TypeError("Duration must be a valid integer.")
        
    def destination(self):
        return str(self.__destination)
    
    def departure(self):
        return str(self.__depdate)

    def duration(self):
        if self.__duration == 1:
            return str(self.__duration) + " day"
        else:
            return str(self.__duration) + " days"
    
    def arrival(self):
        return self.__depdate + self.__duration
    
    def overlaps(self, other):
        if other.__depdate >= self.__depdate and other.__depdate() <= self.arrival():
            return True
        if other.arrival() >= self.__depdate() and other.arrival() <= self.arrival():
            return True
        if self.__depdate >= other.__depdate and self.__depdate() <= other.arrival():
            return True
        if self.arrival() >= other.__depdate() and self.arrival() <= other.arrival():
            return True
        else:
            return False

    def containsweekend(self):
        L = [self.__depdate]
        for i in range(self.__duration):
            L.append(L[-1]+1)
        
        for d in L:
            if d.day_of_week == "Saturday" or d.day_of_week == "Sunday":
                return True
        
        return False
    
    def __str__(self):
        print("Destination: " + self.destination())
        print("Duration: " + self.duration())
        print("Departure: " + self.__depdate.day_of_week() + ", " + self.departure())
        print("Arrival: " + self.arrival().day_of_week() + ", " + self.arrival())
    
    def __repr__(self):
        str(self)
            

        
