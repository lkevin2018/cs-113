"""
Kevin Joseph
RUID: 212003391
Object-Oriented Programming (Spring 2022)
This python file contains the TripSchedule class which is a subclass of the Trip class and the TripScheduleIterator class. The TripSchedule class implementation contains one constructor and 13 methods. The TripScheduleIterator contains one constructor and one method.
"""

from trip import Trip
from date import Date

class TripSchedule(Trip):

    def __init__(self):
        """
        This is the constructor for the TripSchedule class with no parameters. This constructor forms one private instance variable, which is a list to store the Trip objects.
        """
        self.__lst = []
    
    def insert(self, newTrip):
        """
        This method inserts a valid Trip (newTrip) into the TripSchedule object. A valid Trip does not overlap any existing trips and if it does overlap, an Exception is raised.
        """
        for idx in self.__lst:
            if idx.overlaps(newTrip):
                raise Exception("The trip that has been passed through this function overlaps with an existing trip.")
        self.__lst.append(newTrip)

    def delete(self, delTrip):
        """
        This method deletes the first occurance of the valid Trip (delTrip) from the TripSchedule object. Each trip in the TripSchedule is iterated for (non-echanted) and then the indice is used to manually delete the object at the specified index.
        """
        for i in range(len(self)):
            testT = self.__lst[i]
            if testT.departure() == delTrip.departure():
                if testT.destination() == delTrip.destination():
                    if testT.duration() == delTrip.duration():
                        del self.__lst[i]
                        break
    
    def __len__(self):
        """
        This method overloads the len() method of the TripSchedule object and returns the length of the TripSchedule, which is the length of the private instance variable list that stores all of the Trips.
        """
        return len(self.__lst)
    
    def __getitem__(self, idx):
        """
        This method overloads the slice operator of the Trip Schedule object and returns the valid Trip at the index (idx) if the parameter is a valid indice (0 <= idx < len(self)).
        """
        if idx < 0 or idx >= len(self):
            raise IndexError("The index is out of range, please try another valid index.")
        return self.__lst[idx]
    
    def __iter__(self):
        """
        This method overloads the iter() method and returns a iter() object which is handled by the TripScheduleIterator() class. Passes one parameter through: private instance variable list.
        """
        return TripScheduleIterator(self.__lst)
        
    def search(self, keyword):
        """
        This method searches through the TripSchedule object in order to print the results in which the parameter, keyword, matches the month or the destination of the Trip. Before printing the results, they are sorted by departure date using the sortbydeparture() method in this class.
        """
        results = TripSchedule()
        if type(keyword) == int:
            for idx in self:
                if idx.departure().month() == keyword:
                   results.insert(idx) 
        if type(keyword) == str:
            for idx in self:
                if idx.destination() == keyword:
                   results.insert(idx) 
        results.sortbydeparture()
        for idx in results:
            print(idx)
    
    def available(self, month, year):
        """
        This method searches through the TripSchedule using the month and year passed through the parameter to return a list of valid, available, free dates in which the TripSchedule has no Trips scheduled for. Returns a list of valid Date objects.
        """
        takenDates = []
        for trip in self:
            for i in range(trip.duration() + 1):
                takenDates.append(trip.departure() + i)
        for idx in takenDates:
            if idx.year() != year or idx.month() != month:
                takenDates.remove(idx)
        monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        availableDates = []
        dateCounter = Date(month, 1, year)
        if dateCounter.year_is_leap():
            monthDays[1] = 29
        for i in range(monthDays[month-1]):
            if dateCounter not in takenDates:
                availableDates.append(dateCounter)
            dateCounter += 1
        return availableDates
    
    def weekend_travel(self, yr):
        """
        This method returns a list of Trips in which the Trip contains weekend travel during the specified year (yr). Implements the containsweekend() method from the superclass and sorts the list before returning it. Returns a valid list of Trip objects. 
        """
        t1 = TripSchedule()
        for trip in self:
            if trip.containsweekend() and trip.departure().year() == yr:
                t1.insert(trip)
        t1.sortbydeparture()
        return t1.__lst

    def earliest(self):
        """
        This method returns the earliest Trip of the TripSchedule object.
        """
        self.sortbydeparture()
        return self.__lst[0]

    def last(self):
        """
        This method returns the last Trip of the TripSchedule object.
        """
        self.sortbydeparture()
        return self.__lst[-1]

    def sortbydeparture(self):
        """
        This method modifies the private instance variable list in order to sort it using a lambda expression. Sorts each Trip by its respective departure date using the .daycount() method.
        """
        self.__lst.sort(key = lambda x: x.departure().daycount())

    def __str__(self):
        """
        This method overloads the str() method of the TripSchedule object. Returns a valid String representation of the object with appropriate spacing and implementing the str() method of each Trip from its superclass.
        """
        astr = "Trip Schedule: \n \n"
        for trip in self:
            astr += str(trip)
            astr += '\n \n'
        return astr

    def __repr__(self):
        """
        Returns a valid String and overloads repr().
        """
        return(str(self))

class TripScheduleIterator():

    def __init__(self, other):
        """
        This is the constructor of the TripScheduleIterator class. This requires one parameter which is the TripSchedule private instance variable list. This also produces an instance variable called idx in order to store the index that next() relies on.
        """
        self.__iterlst = other
        self.idx = -1
    
    def __next__(self):
        """
        This method overloads the next() method. This raises the StopIteration if the next object being called is out of bounds. Returns the next Trip object in TripSchedule.
        """
        if self.idx > len(self.__iterlst) - 2:
            raise StopIteration
        self.idx += 1
        return self.__iterlst[self.idx]
        