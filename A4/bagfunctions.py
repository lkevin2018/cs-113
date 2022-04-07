"""
bagfunctions.py
Author: Kevin Joseph
RUID: 212003391
"""

from bag import Bag

def remove_item(B, item):
    """
    Function removes all occurances of item (item) in Bag object (B). Modifies B.
    """
    count = B.count(item)
    while count != 0:
        B.erase_one(item)
        count -= 1

def remove_repeats(B):
    """
    Function removes all repeated items in Bag object (B). Modifies B.
    """
    contents = B.items()
    newContents = []
    for idx in contents:
        if idx in newContents:
            B.erase_one(idx)
        else:
            newContents.append(idx)
    for jdx in newContents:
        remove_item(B, jdx)
    for kdx in newContents:
        B.insert(kdx)
            
def mode(B):
    """
    Function returns the mode of the Bag object (B). Does not modifiy B.
    """
    tempDict = {}
    tempKeys = B.items()
    tempValues = []
    for i in range(len(tempKeys)):
        count = B.count(tempKeys[i])
        tempValues.append(count)
    
    highestOccurance = tempValues[0]
    modeList = []
    for j in range(len(tempKeys)):
        if tempValues[j] >= highestOccurance:
            highestOccurance == tempValues[j]
    for k in range(len(tempKeys)):
        if tempValues[k] == highestOccurance:
            modeList.append(tempKeys[k])
    return modeList

def union(B1, B2):
    """
    Function returns the union of two Bag objects (B1 and B2). Returns a new bag object.
    """
    keysB1 = B1.items()
    keysB2 = B2.items()

    valuesB1 = []
    valuesB2 = []

    for idx in keysB1:
        valuesB1.append(B1.count(idx))

    for idx in keysB2:
        valuesB2.append(B2.count(idx))

    contentsB1 = []
    contentsB2 = []

    for i in range(len(valuesB1)):
        for j in range(i):
            contentsB1.append(keysB1[i]*i)

    for i in range(len(valuesB2)):
        for j in range(i):
            contentsB1.append(keysB2[i]*i)

    retBag = Bag()
    
    for idx in contentsB1:
        retBag.insert(idx)
    
    for idx in contentsB2:
        retBag.insert(idx)

    return retBag

def intersection(B1, B2):
    """
    Function returns the intersection of two Bag objects (B1 and B2). Returns a new bag object.
    """
    contentsB1 = B1.items()
    contentsB2 = B2.items()

    retBag = Bag()

    for idx in contentsB1:
        if idx in contentsB2:
            if idx not in retBag.items():
                retBag.insert(idx)
            
    return retBag


