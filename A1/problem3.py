# Kevin Joseph
# RUID: 212003391
def int_to_text(N):
    intDict = {0: '', 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', 100:'one hundred', 200:'two hundred', 300:'three hundred', 400:'four hundred', 500:'five hundred', 600:'six hundred', 700:'seven hundred', 800:'eight hundred', 900:'nine hundred'}
    ans = ""
    while True:
        if N == 1000:
            return "one thousand"
            N = N-1000
        elif N >= 100:
            hundreds = int(str(N)[0]) * 100
            ans = ans + intDict.get(hundreds)
            N = N - hundreds
        elif N >= 20:
            tens = int(str(N)[0]) * 10
            ans = ans + " " + intDict.get(tens)
            N = N - tens
        elif N < 20:
           ans = ans + " " + intDict.get(N)
           return ans
        else: 
            return "Please try again, not a valid number."
      