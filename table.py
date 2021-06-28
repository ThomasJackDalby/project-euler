"""table.py"""

import math

NUMBER_OF_PROBLEMS = 500
COLUMNS = 10
rows = math.ceil(NUMBER_OF_PROBLEMS / COLUMNS)

lines = [
    "| "*COLUMNS+"|",
    "| --- "*COLUMNS+"|",
]

current_line = ""
for i in range(1, NUMBER_OF_PROBLEMS):
    current_line += f"| [{i:03d}]({i:03d}.py) "
    if i % COLUMNS == 0:
        current_line += "|"
        lines.append(current_line)
        current_line = ""

for line in lines:
    print(line)

# with open("table.md", "w") as file:
#     file.writelines(lines)