"""
    Problem 17
    ==========
    
    If the numbers 1 to 5 are written out in words: one, two, three, four,
    five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
    
    If all the numbers from 1 to 1000 (one thousand) inclusive were written
    out in words, how many letters would be used?
    
    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
    forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
    20 letters. The use of "and" when writing out numbers is in compliance
    with British usage.
    
    Answer: 6a979d4a9cf85135408529edc8a133d0
    
"""
from common import check

PROBLEM_NUMBER = 17
ANSWER_HASH = "6a979d4a9cf85135408529edc8a133d0"

teens = {
    11 : "eleven",
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen",
    15 : "fifteen",
    16 : "sixteen",
    17 : "seventeen",
    18 : "eighteen",
    19 : "nineteen",
}

digits_map = {
    1 : "one",
    2 : "two",
    3 : "three",
    4 : "four",
    5 : "five",
    6 : "six",
    7 : "seven",
    8 : "eight",
    9 : "nine",
}
tens_map = {
    1 : "ten",
    2 : "twenty",
    3 : "thirty",
    4 : "forty",
    5 : "fifty",
    6 : "sixty",
    7 : "seventy",
    8 : "eighty",
    9 : "ninety",
}
HUNDRED = "hundred"
THOUSAND = "thousand"

def number_to_text(number):
    digits = int(number % 10)
    tens = int(((number - digits) % 100) / 10)
    hundreds = int(((number - tens - digits) % 1000 ) / 100)
    thousands = int(((number - hundreds - tens - digits) % 10000) / 1000)

    word = ""
    if thousands > 0:
        word += f"{digits_map[thousands]} {THOUSAND}" 
    if hundreds > 0:
        word += f" {digits_map[hundreds]} {HUNDRED}" 
    if (tens > 0 or digits > 0) and (thousands > 0 or hundreds > 0):
        word += " and"
    if tens > 0:
        if tens == 1 and digits > 0:
            teen = 10 + digits
            word += f" {teens[teen]}"
            return word
        else:
            word += f" {tens_map[tens]}"
    if digits > 0:
        if tens < 1:
            word += " "
        word += f"{digits_map[digits]}"

    return word

total = 0
for i in range(1, 1001):
    word = number_to_text(i)
    total += sum((1 for c in word if c != " "))

check(total, PROBLEM_NUMBER, ANSWER_HASH)
