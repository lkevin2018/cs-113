## problem1.py
## Author: Kevin Joseph
## RUID: 212003391

def replace_char(astr, old_char, new_char):
    '''
    This function has three parameters, astr which is a string that has an old character (old_char) which needs to be replaced with a new character (new_char) using recursion. Function returns new, modified string.
    '''
    if len(astr) == 1:
        if astr[0] == old_char:
            return new_char
        else:
            return astr[0]
    elif astr[0] == old_char:
        return new_char + replace_char(astr[1:], old_char, new_char)
    else:
        return astr[0] + replace_char(astr[1:], old_char, new_char)

def occurrences(astr, substr):
    '''
    This function has two parameters and is meant to count the number of times a substring (substr) occurs in a string (astr) using recursion. Function returuns occurances.
    '''
    if len(astr) == len(substr):
        if astr[0:len(substr)] == substr:
            return 1
        else:
            return 0
    elif astr[0:len(substr)] == substr:
        return 1 + occurrences(astr[1:], substr)
    else:
        return 0 + occurrences(astr[1:], substr)  

def inverse_pair(L):
    '''
    This function has one parameter and it is meant to check whether or not any two numbers (a pair) exists in a list L using recursion. Functions returns either True or False
    '''
    if len(L) < 2:
        return False
    if L[0] + L[1] == 0:
        return True
    else:
        return inverse_pair([L[0]] + L[2:]) or inverse_pair(L[1:])
