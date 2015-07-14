from math import *
from tools import *

def problem001():
    """ If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
        Find the sum of all the multiples of 3 or 5 below 1000."""
    sum = 0
    for i in range(1,1000):
        fact3 = isFactor(i,3)
        fact5 = isFactor(i,5)
        if (fact3 or fact5):
            sum = sum + i  
    return sum

def problem002():
    """ Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
        1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
        By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms. """
    sum = 0
    fib_last = 1
    fib_current = 1
    while (fib_current < 4000000):
        fib_next = fib_current + fib_last

        if (isEven(fib_current)):
            sum = sum + fib_current

        fib_last = fib_current
        fib_current = fib_next
    return sum

def problem003():
    """ The prime factors of 13195 are 5, 7, 13 and 29.
        What is the largest prime factor of the number 600,851,475,143? """
    value = 600851475143
    prime = 2
    maxPrime = prime
    while (value != 1):            
        if (isFactor(value, prime)):
            value = value / prime           
            prime = 2
        else:
            prime = nextPrime(prime)
            if (prime > maxPrime):
                maxPrime = prime
    return maxPrime

def problem004():
    """ A palindromic number reads the same both ways. The largest palindrome made from the product of two 2 digit numbers is 9009 = 91 x 99.
	Find the largest palindrome made from the product of two 3 digit numbers. """
    palindrone = 999*999
    while(True):
        palindrone = nextSmallestPalindrone(palindrone)
        factor = 999
        while (factor > 1):
            if (isFactor(palindrone, factor)):
                if (len(str(factor)) == 3):
                    factorb = int(palindrone / factor)
                    if (isFactor(palindrone, factorb)):
                        if (len(str(factorb)) == 3):
                            return palindrone
                if (len(str(palindrone)) < 3):
                    break
            factor = factor -1

def problem005():
    """ 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? """
    test = 1
    current_min = 20
    while(True):
        isAnswer = True
        for factor in range(20,1,-1):
            if (factor < current_min):
                print("Min: " + str(current_min))
                current_min = factor
            if (isFactor(test,factor) == False):
               isAnswer = False
               break
        if (isAnswer):
            return test
        else:
            test = test + 1

def problem006():
    """ The sum of the squares of the first ten natural numbers is,
    1^2 + 2"2 + ... + 10"2 = 385
    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 552 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 ? 385 = 2640.
    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum. """

    # First find sum of each squared
    sum_individually_squared = 0
    for i in range(1,101):
        sum_individually_squared = sum_individually_squared + i * i

    # Next find sum of all squared
    sum_global_squared = 0
    for i in range(1,101):
        sum_global_squared = sum_global_squared + i
    sum_global_squared = sum_global_squared * sum_global_squared

    difference = sum_global_squared - sum_individually_squared
    return difference

def problem007():
    """ By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10 001st prime number? """

    primes = [2]
    num_of_primes = 1
    num = 1
    while(True):
        num = num + 1
        isPrime = True
        for prime in primes:
            if (isFactor(num, prime)):
                isPrime = False
                break
        if isPrime:
            primes.append(num)
            num_of_primes = num_of_primes + 1
            print(str(num_of_primes))
            if (num_of_primes == 10001):
                return primes.pop()
                
def problem008():
    sample = """73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""

    sample = sample.replace('\n','')
    sample = sample.replace('\r','')
    
    number_of_integers = 13
    sample_size = len(sample)

    max_value = 0
    for i in range(1,sample_size - number_of_integers+1):
        value =1
        for j in range(i,i+number_of_integers):
            num = int(sample[j])
            value = value * num
            if (value > max_value):
                max_value = value
    return max_value

def problem009():
    a = 1
    b = 1
    while(True):
        if (isTriplet(a,b)):
            c = (a*a + b*b)**(0.5)
            print("a: " + str(a) + " b: " + str(b) + " c: " + str(c))
            sum = a+b+c
            if (sum == 1000):
                return a*b*c
        if (b < 400):
            b = b + 1
        else:
            b = 1
            a = a + 1 
    
def problem010old():
    # Create the wheel
    known_primes = [ 2, 3, 5, 7, 11, 13 ]   
    number_of_wheels = 3
    target = 2000000

    for i in range(1,4):
        print("Known primes: " + str(known_primes))

        print("-- Iteration --")
        wheel_len = sum(known_primes) * number_of_wheels
        print("Len " + str(wheel_len))
        test_primes = []
        found_primes = []
        for i in range(0,wheel_len):
            test_primes.append(True)

        print("Strike out known primes")
        for prime in known_primes:
            i = 2
            while(True):
                if ((i*prime) > wheel_len):
                    break
                if ((i*prime) > target):
                    break
                test_primes[(i*prime)-1] = False
                i = i + 1

        print("Test remaining probable primes fully")
        for i in range(1,wheel_len):
            if (i > target):
                break
            if (test_primes[i] == True):
                if (isPrime(i+1, found_primes) == False):
                    test_primes[i] = False
                else:
                    print(str(i+1))
                    known_primes.append(i+1)
                    found_primes.append(i+1)
        print("Found primes: " + str(found_primes))
    print("Known primes: " + str(known_primes))
   
def problem010():

    number_of_primes = 2000000
    primes = []
    numbers = []
    print("Generating list")
    for i in range(0,number_of_primes):
        numbers.append(True)

    print("Solving for Primes")
    for i in range(1,number_of_primes):
        if (numbers[i] == True):
            print("Found prime: " + str(i+1))
            primes.append(i+1)
            j = 2
            while(True):
                factor = j * (i+1)
                if (factor > number_of_primes):
                    break
                numbers[factor-1] = False
                j = j + 1

    sum = 0
    for prime in primes:
        sum = sum + prime

    print(primes[-1])
    return sum


