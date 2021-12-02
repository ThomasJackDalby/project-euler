"""
    Problem 42
    ==========
    
    
    The n^th term of the sequence of triangle numbers is given by, t[n] =
    ½n(n+1); so the first ten triangle numbers are:
    
    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
    
    By converting each letter in a word to a number corresponding to its
    alphabetical position and adding these values we form a word value. For
    example, the word value for SKY is 19 + 11 + 25 = 55 = t[10]. If the word
    value is a triangle number then we shall call the word a triangle word.
    
    Using [1]words.txt, a 16K text file containing nearly two-thousand common
    English words, how many are triangle words?
    
    
    Visible links
    1. words.txt
    Answer: 82aa4b0af34c2313a562076992e50aa3
"""
import os
from common import check
from itertools import count, takewhile

PROBLEM_NUMBER = 42
ANSWER_HASH = "82aa4b0af34c2313a562076992e50aa3"
FILE_NAME = "p042_words.txt"

file_path = os.path.join(os.path.dirname(__file__), FILE_NAME)

def get_score(word):
    return sum((ord(c)-64 for c in word))

triangles = set()
def generate_triangles():
    for i in count(1):
        t = 0.5 * i * (i + 1)
        triangles.add(t)
        yield t

generator = generate_triangles()

def is_triangle(n):
    for t in takewhile(lambda t: t < n, generator):
        pass
    return n in triangles    

with open(file_path, "r") as file:
    line = file.readline()
words = [word.strip("\"") for word in line.strip().split(",")]

result = sum(1 for word in words if is_triangle(get_score(word)))
check(result, PROBLEM_NUMBER, ANSWER_HASH)
