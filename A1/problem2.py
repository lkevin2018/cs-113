#Kevin Joseph
#RUID: 212003391
import random
def craps():
    h1 = '-' * 28
    intro = "Welcome to the Craps program"
    ctr = "{:^100s}"

    print(ctr.format(h1))
    print(ctr.format(intro))
    print(ctr.format(h1))

    bal = 1000
    print("Your initial bank balance is $" + str(bal) + ".")

    while bal > 0:
        wgr = int(input("Enter your wager: "))
        if(wgr > bal):
            wgr = int(input("Your wager was invalid, it must be less than $" + str(bal) + " please try again: "))
        print("Okay, let's play.")
        isGameWin = 0
        isGameWin = play_one_game()
        if isGameWin == 1:
            bal = bal + wgr
        else:
            bal = bal - wgr
        print("Your new bank balance is $" + str(bal))
        if bal < 0:
            print("Sorry, you're broke!")
        else:
            cont = input("Do you want to play again? [y/n]")
            if(cont == 'n'):
                print("Sorry you lost money. Better luck next time!")
                quit()

            
def roll_dice():
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    sum = d1 + d2
    print("You rolled " + str(sum))
    return sum

def play_one_game():
    s = roll_dice()
    point = 0
    if s == 7 or s == 11:
        print("You win!!")
        return 1
    elif s == 2 or s == 3 or s == 12:
        print("Sorry, you lose!")
        return 0
    elif s == 4 or s == 5 or s == 6 or s == 8 or s == 9 or s == 10:
        point = s
        print("Your point is " + str(point))
        newThrow = 0
        while newThrow != 7 and newThrow != point:
            newThrow = roll_dice()
        if newThrow == 7:
            print("Sorry, you lose!")
            return 0
        else:
            print("You win!!")
            return 1

craps()