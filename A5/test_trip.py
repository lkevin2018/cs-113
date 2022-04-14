from date import Date
from trip import Trip

if __name__ == "__main__":

    print("--------------------------------")
    print("    Testing the Trip class")
    print("--------------------------------")
    
    t1 = Trip("Paris", Date(4, 1, 2022), 3)
    t2 = Trip("New York", Date(4, 8, 2022), 5)
    t3 = Trip("Paris", Date(12, 25, 2021), 28)
    t4 = Trip("Dubai", Date(1, 12, 2022), 7)
    t5 = Trip("Barcelona", Date(4, 6, 2022), 6)
    t6 = Trip("Mumbai", Date(7, 3, 2022), 3)
    t7 = Trip("London", Date(3, 15, 2021), 4)

    L = [t1, t2, t3, t4, t5, t6, t7]

    print("Seven Trip instances called t1, t2, t3, t4, t5, t6, and t7 have been created.\n")
    print("***** Testing __str__ for these instances *****\n")
    for t in L:
        print(t)

    print("***** Testing destination(), departure(), duration(), arrival() *****\n")

    print(t1.destination()," ---- ", t1.departure(), " ---- ", t1.duration(), " ---- ", t1.arrival())
    print()

    print("CORRECT ANSWER: ")
    print("Paris  ----  April 1, 2022  ----  3  ----  April 4, 2022\n")

    print(t3.destination()," ---- ", t3.departure(), " ---- ", t3.duration(), " ---- ", t3.arrival())
    print()

    print("CORRECT ANSWER: ")
    print("Paris  ----  December 25, 2021  ----  28  ----  January 22, 2022\n")

    print("***** Testing setDestination(), setDeparture(), setDuration() *****\n")
    t1.setDestination("London")
    t1.setDeparture(Date(3, 31, 2022))
    t1.setDuration(5)

    print(t1.destination()," ---- ", t1.departure(), " ---- ", t1.duration(), " ---- ", t1.arrival())
    print()

    print("CORRECT ANSWER: ")
    print("London  ----  March 31, 2022  ----  5  ----  April 5, 2022\n")

    print("***** Testing overlaps() with trips t1, t2, and t5 *****\n")
    if t1.overlaps(t5):
        print("Trip t1 overlaps with t5. (INCORRECT ANSWER)")
    else:
        print("Trip t1 does not overlap with t5. (CORRECT ANSWER)")        

    if t2.overlaps(t5):
        print("Trip t2 overlaps with t5. (CORRECT ANSWER)")
    else:
        print("Trip t2 does not overlap with t5. (INCORRECT ANSWER)")        

    if t3.overlaps(t4):
        print("Trip t3 overlaps with t4. (CORRECT ANSWER)")
    else:
        print("Trip t3 does not overlap with t4. (INCORRECT ANSWER)")        


    print("\n***** Testing containsweekend() *****\n")
    if t1.containsweekend():
        print("Trip t1 contains a weekend. (CORRECT ANSWER)")
    else: 
        print("Trip t1 does not contain a weekend. (INCORRECT ANSWER)")

    if t2.containsweekend():
        print("Trip t2 contains a weekend. (CORRECT ANSWER)")
    else: 
        print("Trip t2 does not contain a weekend. (INCORRECT ANSWER)")
        
    if t3.containsweekend():
        print("Trip t3 contains a weekend. (CORRECT ANSWER)")
    else: 
        print("Trip t3 does not contain a weekend. (INCORRECT ANSWER)")

    if t7.containsweekend():
        print("Trip t7 contains a weekend. (INCORRECT ANSWER)")
    else: 
        print("Trip t7 does not contain a weekend. (CORRECT ANSWER)")

    print("\nThat's all for the Trip class.....\n")
