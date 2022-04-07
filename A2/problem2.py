import pprint
"""
Author: Kevin Joseph
RUID: 212003391
Module for Problem 2, Homework 2
Object Oriented Programming (50:198:113), Spring 2022
"""

def customer_dictionary(balfilename):
    """
    This function has one param, balfilename. The .dat file is passed through in order to produce a dictionary with a key:value pair of each tracked asset of each bank account. Every key is generated to begin with a default value of [] as the pair. The key has a list as its pair which is then iterated through in following functions.
    """
    inf = open(balfilename, "r")
    retDict = {'ACCT#': [], 'SSN':[], 'PREVBAL': [], 'DEPOSITS': [], 'WITHDRAWALS': [], 'MAXDEP': [], 'MAXWDRAW': [], 'INTEREST': [], 'PENALTY': [], 'NEWBAL': []}
    for line in inf:
        ssnNum, acctNum, prevbalNum = line.split()
        retDict['SSN'].append(ssnNum)
        retDict['ACCT#'].append(acctNum)
        retDict['PREVBAL'].append(prevbalNum)
        retDict['DEPOSITS'].append(0.00)
        retDict['WITHDRAWALS'].append(0.00)
        retDict['MAXDEP'].append(0.00)
        retDict['MAXWDRAW'].append(0.00)
        retDict['INTEREST'].append(0.00)
        retDict['PENALTY'].append(0.00)
        retDict['NEWBAL'].append(0.00)

    inf.close()
    return retDict

def update_customer_dictionary(cdictionary, transfilename):
    """
    This function is used with two parameters, cdictionary and transfilename. The cdictionary is the dictionary as a result of the first function and the transfilename parameter is used to update it and ensure that the (1) new Balance is created and the (2) proper interest/penalty is calculated if necessary.
    """
    transfile = open(transfilename, "r") 
    for line in transfile:
        acctNum, trans = line.split()
        if float(trans) > 0.0:
            for i in range(len(cdictionary['ACCT#'])):
                if (cdictionary['ACCT#'])[i] == acctNum:
                    if float(trans) > (cdictionary['MAXDEP'])[i]:
                        (cdictionary['MAXDEP'])[i] = float(trans)
                    (cdictionary['DEPOSITS'])[i] += float(trans)
                    (cdictionary['DEPOSITS'])[i] = round((cdictionary['DEPOSITS'])[i], 2)
                
        else:
            for i in range(len(cdictionary['ACCT#'])):
                if (cdictionary['ACCT#'])[i] == acctNum:
                    if abs(float(trans)) > (cdictionary['MAXWDRAW'])[i]:
                        (cdictionary['MAXWDRAW'])[i] = abs(float(trans))
                    (cdictionary['WITHDRAWALS'])[i] += abs(float(trans))
                    (cdictionary['WITHDRAWALS'])[i] = round((cdictionary['WITHDRAWALS'])[i], 2)
    transfile.close()

    for i in range(len(cdictionary['ACCT#'])):
        (cdictionary['NEWBAL'])[i] = round((float((cdictionary['PREVBAL'])[i])), 2)
        (cdictionary['NEWBAL'])[i] = round((cdictionary['NEWBAL'])[i], 2)
        (cdictionary['NEWBAL'])[i] += round((float((cdictionary['DEPOSITS'])[i])), 2)
        (cdictionary['NEWBAL'])[i] = round((cdictionary['NEWBAL'])[i], 2)

        (cdictionary['NEWBAL'])[i] -= round((float((cdictionary['WITHDRAWALS'])[i])), 2)
        (cdictionary['NEWBAL'])[i] = round((cdictionary['NEWBAL'])[i], 2)

        if float((cdictionary['NEWBAL'])[i]) > 3000.00:
            cash = float((cdictionary['NEWBAL'])[i])
            (cdictionary['INTEREST'])[i] += round((cash*.02), 2)
            (cdictionary['NEWBAL'])[i] += (cdictionary['INTEREST'])[i]
            (cdictionary['NEWBAL'])[i] = round((cdictionary['NEWBAL'])[i], 2)           
        if float((cdictionary['NEWBAL'])[i]) < 100.00:
            (cdictionary['PENALTY'])[i] += 10.00
            (cdictionary['NEWBAL'])[i] -= float((cdictionary['PENALTY'])[i])
            (cdictionary['NEWBAL'])[i] = round((cdictionary['NEWBAL'])[i], 2)

def new_balance_files(cdictionary, summfilename, newbalfilename):
    """
    This function has three parameters: cdictionary, summfilename, and newbalfilename. The cdictionary is the customer dictionary created and updated by the prior functions. The summfilname parameter is the output of this function which produces a .dat file with the detailed summary of each account along with all of its assets and identifiers. The newbalfilename had the SSN ACCT# AND NEWBAL associated with each account.
    """
    summ = open(summfilename, "w")
    newb = open(newbalfilename, "w")
    summ.write("ACCT#  SSN       PREVBAL  DEPOSITS  WITHDRAWALS   MAXDEP  MAXWDRAW  INTEREST  PENALTY   NEWBAL \n")
    summ.write(95*'-' + '\n')
    for i in range(len(cdictionary['ACCT#'])):
        summ.write("{0:<10} {1:<16} {2:<10} {3:<10} {4:<13} {5:<10} {6:<10} {7:<11} {8:<10} {9:<10} {10}".format((cdictionary['ACCT#'])[i], (cdictionary['SSN'])[i], (cdictionary['PREVBAL'])[i], (cdictionary['DEPOSITS'])[i], (cdictionary['WITHDRAWALS'])[i], (cdictionary['MAXDEP'])[i], (cdictionary['MAXWDRAW'])[i], (cdictionary['INTEREST'])[i], (cdictionary['PENALTY'])[i], (cdictionary['NEWBAL'])[i], '\n'))
    summ.close()
    
    for j in range(len(cdictionary['ACCT#'])):
        newb.write((cdictionary['SSN'])[j] + "       " + (cdictionary['ACCT#'])[j] + "       " + str((cdictionary['NEWBAL'])[j]) + '\n')
    newb.close()

if __name__ == "__main__":
    print("Running the problem2 module (Bank Transactions problem)\n")
    cdict = customer_dictionary("balance.dat")
    pdate_customer_dictionary(cdict, "transactions.dat")
    new_balance_files(cdict, "transsummary.dat", "newbalance.dat")
    print("Updated bank balance data appears in the files transsummary.dat and newbalance.dat")
    print("Goodbye!\n")