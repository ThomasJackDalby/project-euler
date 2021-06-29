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

for line in lines:
    print(line)

# with open("table.md", "w") as file:
#     file.writelines(lines)