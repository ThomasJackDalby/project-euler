def isEven(number):
    return isFactor(number, 2)

def isFactor(number, factor):
    return (number%factor == 0)

def isTriplet(a,b):
    if (b < a):
        return False
    cc = a*a + b*b
    c = cc ** (0.5)
    return (c == round(c))

def nextSmallestPalindrone(palindrone):
    palindrone = palindrone - 1
    while (isPalindrome(palindrone) == False):
        palindrone = palindrone - 1
    return palindrone

def isPalindrome(number):
    numberString = str(number)
    length = len(numberString)
    i = 0
    while (i < len(numberString) / 2.0):
        a = numberString[i]
        b = numberString[length - 1 - i]
        if (a != b):
            return False
        i = i + 1
    return True

def isPrime(number):
    for i in range(2,number):
        if (isFactor(number, i)):
            return False
    return True

def isPrime(number, primelist):
    for i in primelist:
        if (isFactor(number, i)):
            return False
    return True

def nextPrime(number):
    while(True):
        number = number + 1
        if (isPrime(number)):
            return number

def numberToWord(number):
    word = ""
    
    if (number < 10):
        return singleNumberToWord(str(number))
    if (number == 10):
        return "ten"
    if (number < 20):
        return teenToWord(str(number))
    

    for i in range(0,len(str(number))):

        

        char = singleNumberToWord(str(number)[i])
        if (char == None):
            char = "unknown"
        word += " " + char
    return word
  
def switch(sample, keys, values):
    for i in range(0, len(keys)):
        if (sample == keys[i]):
            return values[i]
    return None    
  
def singleNumberToWord(number):
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    values = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    return switch(int(number), keys, values)
 
def powersOfTenToWord(number):
    keys = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    values = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninty"]
    return switch(int(number), keys, values)

