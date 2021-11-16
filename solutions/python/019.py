# COMPLETED
"""
    Problem 19
    ==========
    
    You are given the following information, but you may prefer to do some
    research for yourself.
    
    • 1 Jan 1900 was a Monday.
    • Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    • A leap year occurs on any year evenly divisible by 4, but not on a
    century unless it is divisible by 400.
    
    How many Sundays fell on the first of the month during the twentieth
    century (1 Jan 1901 to 31 Dec 2000)?
    
    Answer: a4a042cf4fd6bfb47701cbc8a1653ada
    
"""
from common import check

PROBLEM_NUMBER = 19
ANSWER_HASH = "a4a042cf4fd6bfb47701cbc8a1653ada"

WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

def get_days_in_month(month, year):
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if year % 4 == 0:
            if year % 100 == 0:
                return 28 if year % 400 == 0 else 27
            return 28
        return 27
    else:
        return 31
        
days = 0
day = 1
month = 1
year = 1900
total = 0
days_in_month = get_days_in_month(month, year)
keep_going = True
start_counting = False
while keep_going:
    weekday = days % 7
    if not start_counting and day == 1 and month == 1 and year == 1901:
        start_counting = True
    elif day == 31 and month == 12 and year == 2000:
        keep_going = False
        break
    day += 1
    days += 1
    if day > days_in_month:
        month += 1
        day = 1
        if month > 12:
            month = 1
            year += 1
        days_in_month = get_days_in_month(month, year)
    
    if start_counting and weekday == 6 and day == 1:
        total += 1

check(total, PROBLEM_NUMBER, ANSWER_HASH)