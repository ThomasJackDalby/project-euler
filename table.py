"""table.py"""

import math, os

NUMBER_OF_PROBLEMS = 500
COLUMNS = 10
rows = math.ceil(NUMBER_OF_PROBLEMS / COLUMNS)

lines = [
    "| "*COLUMNS+"|",
    "| --- "*COLUMNS+"|",
]

current_line = ""
for i in range(1, NUMBER_OF_PROBLEMS):
    file_path = f"src/{i:03d}.py"
    add_link = False
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            file_line = file.readline()
            add_link = file_line.startswith("# COMPLETED")

    current_line += f"| [{i:03d}]({file_path}) " if add_link else f"| {i:03d} "
    if i % COLUMNS == 0:
        current_line += "|"
        lines.append(current_line)
        current_line = ""

with open("README.md", "r") as file:
    readme_lines = file.readlines()

found = False
for line_number in range(len(readme_lines)):
    line = readme_lines[line_number]
    if line.startswith("## Progress"):
        found = True
        break
if found == False:
    print("Error")
else:
    prefix_lines = readme_lines[:line_number+2]
    for line in prefix_lines:
        print(line)