import sys

from date import Date
from trip import Trip
from tripschedule import TripSchedule


if __name__ == "__main__":

    print("---------------------------------------")
    print("    Testing the TripSchedule class")
    print("---------------------------------------")
    
    t1 = Trip("Paris", Date(4, 1, 2022), 3)
    t2 = Trip("New York", Date(4, 8, 2022), 5)
    t3 = Trip("Dubai", Date(4, 29, 2022), 7)
    t4 = Trip("Paris", Date(12, 3, 2021), 8)
    t5 = Trip("Madrid", Date(4, 15, 2021), 6)
    t6 = Trip("Damascus", Date(5, 20, 2022), 3)
    t7 = Trip("Barcelona", Date(4, 6, 2022), 6)
    t8 = Trip("Melbourne", Date(12, 18, 2022), 14)

    S = TripSchedule()
    S.insert(t1)
    S.insert(t3)
    S.insert(t2)
    S.insert(t6)
    S.insert(t4)
    S.insert(t8)
    S.insert(t5)

    answer = input("Ready to start testing? [y/n] ")
    if answer != 'y':
        sys.exit()

    print("Here are all the trips currently in the schedule (checking __getitem__ and __len__):\n")

    for i in range(len(S)):
        print(S[i])

    answer = input("Ready for next test? [y/n] ")
    if answer != 'y':
        sys.exit()        

    print("Here's the schedule again. Now checking iter() and next(): ")

    try:
        i = iter(S)        
        while True:
            print(next(i))
    except StopIteration:
        print("\nStopIteration exception was correctly caught by next()\n")
    except:
        print("\nERROR: Something is wrong in iter() and/or next()\n")

    answer = input("Ready for next test? [y/n] ")
    if answer != 'y':
        sys.exit()        
    
    try:
        print("Trying to insert Trip t7....")
        S.insert(t7)
    except:
        print("\nEXCEPTION CAUGHT: cannot insert Trip t7. (This is correct.)\n")
    else:
        print("\nERROR: Trip t7 is a conflict. An exception should have been raised.\n")

    answer = input("Ready for next test? [y/n] ")
    if answer != 'y':
        sys.exit()        

    print("Testing the search() method. All trips in the month of April in the schedule are shown below: ")
    S.search(4)
    print()

    print("Testing the search() method. All trips to Paris in the schedule are shown below: ")    
    S.search("Paris")
    print()

    answer = input("Ready for next test? [y/n] ")
    if answer != 'y':
        sys.exit()    

    print("Deleting the following trip from the schedule: ")
    print(t6)
    print()
    S.delete(t6)

    print("The modified schedule is shown below:")
    
    for trip in S:
        print(trip)

    answer = input("Ready for next test? [y/n] ")
    if answer != 'y':
        sys.exit()        

    print("Testing the available() method. No travel is scheduled on the following days in April, 2022: ")

    L = S.available(4, 2022)
    for d in L:
        print(d)

    answer = input("Ready for next test? [y/n] ")
    if answer != 'y':
        sys.exit()        

    print("\nTesting the weekend_travel() method. Trips in 2022 that involve weekend travel are listed below:\n")

    L = S.weekend_travel(2022)
    for t in L:
        print(t)

    answer = input("Ready for next test? [y/n] ")
    if answer != 'y':
        sys.exit()
        

    print("\nTesting the earliest() method. The trip in the schedule with the earliest departure date is: \n")

    etrip = S.earliest()
    print(etrip)

    answer = input("Ready for next test? [y/n] ")
    if answer != 'y':
        sys.exit()
    

    print("\nTesting the last() method. The trip in the schedule with the last departure date is: \n")

    ltrip = S.last()
    print(ltrip)

    answer = input("Ready for next test? [y/n] ")
    if answer != 'y':
        sys.exit()

    print("\nTesting the sortbydeparture() method. The schedule has been sorted by departure date and is shown below: \n") 

    S.sortbydeparture()
    print(S)    

    print("\nAnd that's all, folks!\n")



