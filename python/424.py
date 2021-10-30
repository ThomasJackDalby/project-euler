"""
    Problem 424
    ===========
    
    The above is an example of a cryptic kakuro (also known as cross sums, or
    even sums cross) puzzle, with its final solution on the right. (The common
    rules of kakuro puzzles can be found easily on numerous internet sites.
    Other related information can also be currently found at [1]krazydad.com
    whose author has provided the puzzle data for this challenge.)
    
    The downloadable text file ([2]kakuro200.txt) contains the description of
    200 such puzzles, a mix of 5x5 and 6x6 types. The first puzzle in the file
    is the above example which is coded as follows:
    
    6,X,X,(vCC),(vI),X,X,X,(hH),B,O,(vCA),(vJE),X,(hFE,vD),O,O,O,O,(hA),O,I,(hJC,vB),O,O,(hJC),H,O,O,O,X,X,X,(hJE),O,O,X
    
    The first character is a numerical digit indicating the size of the
    information grid. It would be either a 6 (for a 5x5 kakuro puzzle) or a 7
    (for a 6x6 puzzle) followed by a comma (,). The extra top line and left
    column are needed to insert information.
    
    The content of each cell is then described and followed by a comma, going
    left to right and starting with the top line.
    X = Gray cell, not required to be filled by a digit.
    O (upper case letter)= White empty cell to be filled by a digit.
    A = Or any one of the upper case letters from A to J to be replaced by its
    equivalent digit in the solved puzzle.
    ( ) = Location of the encrypted sums. Horizontal sums are preceded by a
    lower case "h" and vertical sums are preceded by a lower case "v". Those
    are followed by one or two upper case letters depending if the sum is a
    single digit or double digit one. For double digit sums, the first letter
    would be for the "tens" and the second one for the "units". When the cell
    must contain information for both a horizontal and a vertical sum, the
    first one is always for the horizontal sum and the two are separated by a
    comma within the same set of brackets, ex.: (hFE,vD). Each set of brackets
    is also immediately followed by a comma.
    
    The description of the last cell is followed by a Carriage Return/Line
    Feed (CRLF) instead of a comma.
    
    The required answer to each puzzle is based on the value of each letter
    necessary to arrive at the solution and according to the alphabetical
    order. As indicated under the example puzzle, its answer would be
    8426039571. At least 9 out of the 10 encrypting letters are always part of
    the problem description. When only 9 are given, the missing one must be
    assigned the remaining digit.
    
    You are given that the sum of the answers for the first 10 puzzles in the
    file is 64414157580.
    
    Find the sum of the answers for the 200 puzzles.
    
    Visible links
    1. http://krazydad.com/
    2. kakuro200.txt
    Answer: c412afe5b5d76dbfbb77443ed5836d89
    
"""
import os
from common import check, get_relative_file_path
from functools import cache
from itertools import permutations as get_permutations

PROBLEM_NUMBER = 424
ANSWER_HASH = "c412afe5b5d76dbfbb77443ed5836d89"
PUZZLES_FILE_NAME = "p424_kakuro200.txt"
puzzles_file_path = get_relative_file_path(__file__, PUZZLES_FILE_NAME)

def load_puzzles(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()
    return [parse_puzzle(line) for line in lines]

class Puzzle:
    def __init__(self, size):
        self.size = size
        self.cells = {}
        self.vertical_groups = {}
        self.horizontal_groups = {}

    def set_cell(self, cell):
        self.cells[cell.position] = cell
        self.horizontal_groups[cell.position] = cell.horizontal_group
        self.vertical_groups[cell.position] = cell.vertical_group
    
    def get_cell(self, x, y):
        if (x, y) in self.cells:
            return self.cells[(x, y)]
        return None

    def get_horizontal_group(self, x, y):
        if (x, y) in self.horizontal_groups:
            return self.horizontal_groups[(x, y)]
        return None

    def get_vertical_group(self, x, y):
        if (x, y) in self.vertical_groups:
            return self.vertical_groups[(x, y)]
        return None

@cache
def calculate_permutations(total, number):
    permutations = set()
    if number == 0:
        return None
    if number == 1:
        return [tuple([total])] if total < 10 else None
    for i in range(1, 10):
        next_total = total - i
        if next_total <= 0:
            continue
        
        child_permutations = calculate_permutations(next_total, number-1)
        if child_permutations is None:
            continue

        for permutation in child_permutations:
            if i in permutation:
                continue
            next_permutation = list(permutation) + [i]
            next_permutation.sort()
            permutations.add(tuple(next_permutation))

    permutations = list(set(permutations))
    permutations.sort()
    return permutations

class CellGroup:
    def __init__(self, letters) -> None:
        self.letters = letters
        self.cells = []
        self.total = 0
    
    def set_mapping(self, mapping):
        total = "".join(mapping[letter] for letter in self.letters)
        self.total = int(total)


    def add_cell(self, cell):
        self.cells.append(cell)

    def update_permutations(self):
        self.permutations = calculate_permutations(self.total, len(self.cells))

class Cell:
    def __init__(self, x, y, value=None) -> None:
        self.x = x
        self.y = y
        self.position = (x, y)
        self.value = value
        self.vertical_group = None
        self.horizontal_group = None

def parse_puzzle(text):
    bits = []
    start = 0
    brackets = False
    for i in range(len(text)):
        char = text[i]
        if not brackets and char == ",":
            bit = text[start:i]
            bits.append(bit)
            start = i+1
        elif not brackets and char == "(":
            brackets = True
        elif brackets and char == ")":
            brackets = False

    size = int(bits[0])
    puzzle = Puzzle(size)
    x, y = 0, 0
    for bit in bits[1:]:
        x += 1
        if x >= size:
            x = 0
            y += 1
        if bit == "X": 
            continue
        if bit[0] == "(":
            continue
        else:
            cell = Cell(x, y)
            if bit != "O":
                cell.value = bit

            horizontal_group = puzzle.get_horizontal_group(x-1, y)
            if horizontal_group is not None:
                cell.horizontal_group = horizontal_group
                horizontal_group.cells.append(cell)

            vertical_group = puzzle.get_vertical_group(x, y-1)
            if vertical_group is not None:
                cell.vertical_group = vertical_group
                vertical_group.cells.append(cell)

            puzzle.set_cell(cell)

def get_available_digits(cell, current_digits):
    h_digits = [current_digits[cell.position] for cell in cell.horizontal_group.cells if cell.position in current_digits]
    h_perms = [p for p in cell.horizontal_group.permutations if all(h_digits, lambda d: d in p)]
    return []

def calculate(values, remaining_cells):
    cell = remaining_cells[0]
    available_digits = []
    if len(available_digits) == 0:
        return None
    for digit in available_digits:
        next_values = dict(values)
        next_values[cell] = digit
        solution = calculate(next_values, remaining_cells[1:])
        if solution is not None:
            return solution

def main():
    puzzles = load_puzzles(puzzles_file_path)
    mappings = ({ l : i for i, l in enumerate(p) } for p in get_permutations("ABCDEFGHIJ", 9))
    for mapping in mappings[:100]:
        print(mapping)

    exit()
    for puzzle in puzzles:
        # every empty cell can have a digit 1 to 9
        # permutations are reduced as digits can only exist once per group
        # they're reduced further as available digits are based on the total and whats left
        # depth first search to save memory
        # try to place digits. if no digits valid for space, reject and go to next attempt
        # track attempts as dictionarys of values
        # need to also track what we've tried?
        # need an order so as not to repeat stuff (and order is not important in the puzzle)

        remaining_cells = puzzle.cells
        values = {}
        solution = calculate(values, remaining_cells)

main()
check(None, PROBLEM_NUMBER, ANSWER_HASH)
