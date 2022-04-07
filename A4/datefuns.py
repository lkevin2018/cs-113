"""
datefuns.py
Author: Kevin Joseph
RUID: 212003391
"""
from date import Date

def weekend_dates(m, y):
    """
    Function prints every weekend date of the specified month (m) and year (y).
    """
    daysOfTheYear = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    wkndDates = []
    if y >= 1800:
        if Date(init_y = y).year_is_leap():
            daysOfTheYear[1] = 29
        if m >= 1 and m <= 12:
            for i in range(1, daysOfTheYear[m-1] + 1):
                if Date(m, i, y).day_of_week() == "Saturday" or Date(m, i, y).day_of_week() == "Sunday":
                    wkndDates.append(Date(m, i, y))
            
    for i in wkndDates:
        print(str(i) + " (" + i.day_of_week() + ")")

def first_mondays(y):
    """
    Function prints every first Monday of the specified year (y).
    """
    mndyDates = []
    for i in range(1, 13):
        for j in range(1, 8):
            if Date(i, j, y).day_of_week() == "Monday":
                mndyDates.append(Date(i, j, y))
    print("First Mondays of " + str(y) + ":" "\n")
    for i in mndyDates:
        print(str(i))

def interval_schedule(start_date, end_date, interval):
    """
    Function returns a list of every valid date after each specific interval (interval) in days after start date (start_date) until end date (end_date) (inclusive).
    """
    retList = [start_date]
    while retList[-1] <= end_date:
        retList.append((retList[-1] + interval))
    if retList[-1] > end_date:
        del retList[-1]
    return retList

