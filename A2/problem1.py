#problem1.py
#Author: Kevin Joseph
#RUID: 212003391
"""
This Programming Assignment generates an Essay Formatting Helper Program which removes extra whitespaces, adjusts line length to a preset value of 60, and produces essay statistics.
"""
if __name__ == "__main__":
    print("Essay Formatting Helper Program \n")
    print(31*'-' + '\n')
    print('\n')
    inpfile = input("Enter the name (*.txt) of the file containing the essay: ")
    filename = inpfile[:-4]
    fileneb = filename + "_neb.txt"
    filefinal = filename + "_final.txt"
    filestats = filename + "_stats.txt"
    print('\n')
    print("The formatted essay is in the file " + filefinal + '\n')
    print("The essay statistics are in the file " + filestats + '\n')

def remove_extra_whitespaces(infile, outfile):
    """
    This function is implemented to remove all of the extra white space between each word of the param infile and exports it to param outfile. It also ensures that there is only one space between each paragraph.
    """
    inf = open(infile, "r") 
    tempf = open(outfile, 'x')
    for line in inf: 
        newL = []
        for i in range(len(line)):
            if i == len(line) - 1 or newL == []:
                if line[i] != " ":
                    newL.append(line[i])
            else:
                if line[i] != " " and line[i-1] != " ":
                    newL.append(line[i])
                elif line[i] == " " and line[i+1] != " ":
                    newL.append(line[i])
                elif line[i] != " ":
                    newL.append(line[i])    
        tempf.writelines(newL)
        tempf.write("\n")
                
    inf.close()
    tempf.close()
    openf = open(outfile, 'r')
    filterL = openf.readlines()
    openf.close()

    filteredf = open(outfile, "w")
    filtL = []
    for j in range(len(filterL)):    
        if j == len(filterL)-1 or filtL == []:
            if filterL[j] != '\n':
                filtL.append(filterL[j])
        elif filterL[j] == '\n' and filterL[j+1] != '\n':
            if (filterL[j+1])[0].isupper():
                filtL.append(filterL[j])
        elif filterL[j] != '\n':
            filtL.append(filterL[j])
    filteredf.writelines(filtL)

    filteredf.close()

def adjust_linelength(infile, outfile):
    """
    This function has two parameters infile and outfile. The function adjusts the linelength so that each line is 60 characters long and exports it into the outfile.
    """
    inf = open(infile, "r")
    L = inf.readlines()
    inf.close()

    outf = open(outfile, "x")
    isRun = True
    i = 0
    while isRun:
        if L[i] != '\n':
            count = len(L[i])
            if i == (len(L)-1):
                isRun = False
            elif count < 60:
                L[i] = (L[i]).strip() + " " + (L[i+1])[:59-count].strip() + '\n'
                if L[i+1] == '\n':
                    i += 1
                else:
                    L[i+1] = (L[i+1])[61-count:]
                    count = len((L[i]))
                    if count < 59 and i < len(L)-1 and L[i+1] != '\n':
                        L.remove(L[i+1])
                        i += 1
                    else:
                        i += 1
            elif count > 60:
                L[i+1] = (L[i])[59:].strip() + " " + L[i+1]
                L[i] = (L[i])[:59].strip() + '\n'  
                i += 1 
            else:
                i += 1
        else:
            i+=1
                   
    outf.writelines(L)
    outf.close()


def essay_statistics(infile, outfile):
    """
    This function generates a statistic file based on the param infile and exports into the param outfile. The function returns the number of non-blank lines, number of words, and average word character count.
    """
    inf = open(infile, "r")
    L = inf.readlines()
    inf.close()

    outf = open(outfile, "x")
    
    numBlankL = 0
    wordLAvg = 0
    wordCount = 0

    for idx1 in L:
        if idx1 != '\n':
            numBlankL += 1
    
    wordCount = wordCount + numBlankL - 1
    
    for line in L:
        for idx2 in line:
            if idx2 == " ":
                wordCount += 1

    avgWordL = []
    for i in range(len(L)):
        lineL = []
        counter = 0
        for j in range(len(L[i])):
            if (L[i])[j] != " " and (L[i])[j] != '\n':
                counter += 1
            else:
                lineL.append(counter)
                counter = 0
        lineSum = 0
        lineAvg = 0
        for idx3 in lineL:
            lineSum += idx3
        lineAvg = lineSum / (len(lineL))
        avgWordL.append(lineAvg)
    
    avgCounter = 0  
    wordLSum = 0
    for idx4 in avgWordL:
        if idx4 != 0.0 and idx4 != 0:
            wordLSum += idx4
            avgCounter += 1
    wordLAvg = int(wordLSum / (avgCounter))
    


    outf.write("In the file " + infile + ":\n")
    outf.write("\n")
    outf.write("Number of (non-blank) lines: " + str(numBlankL) + "\n")
    outf.write("            Number of words: " + str(wordCount) + "\n")
    outf.write("        Average word length: " + str(wordLAvg) + "\n")


    outf.close()


def format_essay():
    """
    This function has no parameters and calls the other functions in the specified order. Returns the files called by the main function.
    """
    remove_extra_whitespaces(inpfile, fileneb)
    adjust_linelength(fileneb, filefinal)
    essay_statistics(filefinal, filestats)
    return inpfile, fileneb, filefinal, filestats

    


format_essay()
       


