
# Euler Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def isFactor(number, factor):
    """ This function calculates if the number is a factor of the other """

    div = float(number) / float(factor)
    if (div == round(div)):
        return True
    else:
        return False


sum = 0
for i in range(1,1000):
    print(str(i), ",")
    fact3 = isFactor(i,3)
    fact5 = isFactor(i,5)
    if (fact3 or fact5):
        sum = sum + i  
    
print(str(sum))


