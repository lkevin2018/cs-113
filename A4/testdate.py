"""
This is a test module for the Date class implementation in date.py
"""

from date import Date

def test_Date_methods():

    print("I have created some instances of the Date class, which are printed below:\n")

    firstdate = Date(1,1,Date.min_year)
    indday = Date(7, 4, 1876)
    xmas = Date(12, 25, 2018)
    millenium = Date(1, 1, 2000)
    leapday = Date(2, 29, 2016)
    lastdate = Date(12, 31, 1999)
    testdate = Date(12, 31, 1999)

    print(firstdate)
    print(indday)
    print(xmas)
    print(millenium)
    print(leapday)
    print(lastdate)

    print("\nTesting the .nextday() method...")
    print("--------------------------------\n")

    print("The date after ", firstdate, "is", firstdate.nextday())
    print("The date after ", indday, "is", indday.nextday())
    print("The date after ", xmas, "is", xmas.nextday())
    print("The date after ", millenium, "is", millenium.nextday())
    print("The date after ", leapday, "is", leapday.nextday())
    print("The date after ", lastdate, "is", lastdate.nextday())    
    

    print("\nTesting the .prevday() method...")
    print("--------------------------------\n")

    print("The date before ", indday, "is", indday.prevday())
    print("The date before ", xmas, "is", xmas.prevday())
    print("The date before ", millenium, "is", millenium.prevday())
    print("The date before ", leapday, "is", leapday.prevday())
    print("The date before ", lastdate, "is", lastdate.prevday())

    print("--------------------------------------------------")
    print("Testing the overloaded operators of the Date class")
    print("--------------------------------------------------\n")

    print("\nTesting the overloaded + operator...")
    print("------------------------------------\n")

    print("365 days after", indday, "the date is", indday + 365, "(CORRECT ANSWER: July 4, 1877)")
    print("7 days after", xmas, "the date is", xmas + 7, "(CORRECT ANSWER: January 1, 2019)")
    print("36500 days after", millenium, "the date is", millenium + 36500, "(CORRECT ANSWER: December 7, 2099)")
    print("1460 days after", leapday, "the date is", leapday + 1460, "(CORRECT ANSWER: February 28, 2020)")
    print("26 days after", lastdate, "the date is", lastdate + 26, "(CORRECT ANSWER: January 26, 2000)")

    print("\nTesting the overloaded - operator...")
    print("------------------------------------\n")

    print("365 days before", indday, "the date is", indday - 365, "(CORRECT ANSWER: July 5, 1875)")
    print("7 days before", xmas, "the date is", xmas - 7, "(CORRECT ANSWER: December 18, 2018)")
    print("36500 days before", millenium, "the date is", millenium - 36500, "(CORRECT ANSWER: January 25, 1900)")
    print("1460 days before", leapday, "the date is", leapday - 1460, "(CORRECT ANSWER: March 1, 2012)")
    print("26 days before", lastdate, "the date is", lastdate - 26, "(CORRECT ANSWER: December 5, 1999)")

    print("\nTesting the overloaded < operator...")
    print("------------------------------------\n")

    if indday < xmas:
        print(indday, "occurs before", xmas, "(CORRECT ANSWER)")
    else:
        print(indday, "does not occur before", xmas, "(INCORRECT ANSWER)")

    if millenium < firstdate:
        print(millenium, "occurs before", firstdate, "(INCORRECT ANSWER)")
    else:
        print(millenium, "does not occur before", firstdate, "(CORRECT ANSWER)")

    if lastdate < millenium: 
        print(lastdate, "occurs before", millenium, "(CORRECT ANSWER)")
    else:
        print(lastdate, "does not occur before", millenium, "(INCORRECT ANSWER)")
        
    print("\nTesting the overloaded == operator...")
    print("-------------------------------------\n")

    lastdate2 = Date(12, 31, 1999)

    if firstdate == lastdate:
        print(firstdate, "equals", lastdate, "(INCORRECT ANSWER)")
    else:
        print(firstdate, "does not equal", lastdate, "(CORRECT ANSWER)")

    if lastdate == lastdate2:
        print(lastdate, "equals", lastdate2, "(CORRECT ANSWER)")
    else:
        print(lastdate, "does not equal", lastdate2, "(INCORRECT ANSWER)")

    print("\nPrinting results of all comparison operators for ", firstdate, "and", leapday, "(check correctness yourself):")
    print("---------------------------------------------------------------------------------------\n")

    print(firstdate, "<", leapday, ":", firstdate < leapday)
    print(firstdate, ">", leapday, ":", firstdate > leapday)
    print(firstdate, "==", leapday, ":", firstdate == leapday)
    print(firstdate, "!=", leapday, ":", firstdate != leapday)
    print(firstdate, "<=", leapday, ":", firstdate <= leapday)
    print(firstdate, ">=", leapday, ":", firstdate >= leapday)

    print("\nAnd that's all, folks! Goodbye!\n")

    print(testdate >= lastdate)
    print(testdate <= lastdate)
    print(testdate == lastdate)
    print(testdate != lastdate)
    
    
if __name__ == "__main__":
    test_Date_methods()
    
