"""
Kevin Joseph
RUID: 212003391
Object-Oriented Programming (Spring 2022)
This python file contains the Trip class which is a subclass of the Date class. This implementation contains one constructor and 11 methods.
"""

from date import Date

class Trip (Date):
    
    def __init__(self, init_destination, init_depdate, init_duration):
        """
        This is the constructor for the Trip class with three parameters: a destination (which must be a valid String), a departure date (which must be a valid Date object), and a duration (which much be a valid integer value >= 1). All of the parameters are set to private instance variables as denoted with the '__.'
        """
        if type(init_destination) == str:
            if type(init_depdate) == Date:
                if type(init_duration) == int and init_duration >= 1:
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
        """
        This method sets the new destination of the Trip object, and checks if the sole parameter is a String before modifying the private instance variable. 
        """
        if type(newDest) == str:
            self.__destination = newDest
        else:
            raise TypeError("Destination must be a string.")
    
    def setDeparture(self, newDepdate):
        """
        This method sets the new departure date of the Trip object, and checks if the sole parameter is a Date before modifying the private instance variable. 
        """
        if type(newDepdate) == Date:
            self.__depdate = newDepdate
        else:
            raise TypeError("Departure Date must be a valid Date object.")
    
    def setDuration(self, newDuration):
        """
        This method sets the new duration of the Trip object, and checks if the sole parameter is a valid Integer >= 1 before modifying the private instance variable. 
        """
        if type(newDuration) == int and newDuration >= 1:
            self.__duration = newDuration
        else:
            raise TypeError("Duration must be a valid integer.")
        
    def destination(self):
        """ 
        This method returns the destination (private instance variable value) of the Trip object. Returns a String object. 
        """
        return self.__destination
    
    def departure(self):
        """ 
        This method returns the departure date (private instance variable value) of the Trip object. Returns a Date object. 
        """
        return self.__depdate

    def duration(self):
        """ 
        This method returns the duration (private instance variable value) of the Trip object. Returns a int value. 
        """
        return self.__duration
    
    def arrival(self):
        """
        This method returns the calculated arrival date using the Superclass ADD method to add the duration to the departure date in order to get the arrival date. Returns a Date object.
        """
        return self.__depdate + self.__duration
    
    def overlaps(self, other):
        """
        This method returns either True or False based on whether or not the current Trip (self) overlaps in any way with another Trip (other). This method has solely one parameter which is other, a valid Trip object to compare to. Returns a boolean value.
        """
        if other.__depdate >= self.__depdate and other.__depdate <= self.arrival():
            return True
        if other.arrival() >= self.__depdate and other.arrival() <= self.arrival():
            return True
        if self.__depdate >= other.__depdate and self.__depdate <= other.arrival():
            return True
        if self.arrival() >= other.__depdate and self.arrival() <= other.arrival():
            return True
        else:
            return False

    def containsweekend(self):
        """ 
        This method returns either True or False based on whether or not the current Trip (self) contains a weekend in the span of the Trip. Returns a boolean value.
        """
        L = [self.__depdate]
        for i in range(self.__duration):
            L.append(L[-1]+1) 
        for d in L:
            if d.day_of_week() == "Saturday" or d.day_of_week() == "Sunday":
                return True
        return False
    
    def __str__(self):
        """
        This method returns the String representation of the Trip object. The formatting contains the Destination, Duration, Departure (with day of the week), and Arrival (with day of the week). Returns a valid String and overloads str.
        """
        l1 = ("Destination: " + str(self.destination()))
        l2 = ("Duration: ")
        if self.__duration == 1:
            l2 += str(self.__duration) + " day"
        else:
            l2 += str(self.__duration) + " days"
        l3 = ("Departure: " + self.__depdate.day_of_week() + ", " + str(self.departure()))
        l4 = ("Arrival: " + self.arrival().day_of_week() + ", " + str(self.arrival()))
        return l1 + '\n' + l2 + '\n' + l3 + '\n' + l4
    
    def __repr__(self):
        """
        Returns a valid String and overloads repr().
        """
        return str(self)
            

        
