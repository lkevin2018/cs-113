#Kevin Joseph
#RUID: 212003391
import math

def multi_column_print(L, numcols):
    rows = math.ceil(len(L)/numcols)
    count = 0
    for x in range(rows):
        for x in range(numcols):
            while count < len(L):
                if count%numcols == 1:
                    print(L[count])
                else:
                    print(L[count], end ="       ")
            
                count = count + 1