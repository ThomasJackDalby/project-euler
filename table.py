"""table.py"""

import math, os

PYTHON_FOLDER_NAME = "python"
GO_FOLDER_NAME = "go"
NUMBER_OF_PROBLEMS = 500
COLUMNS = 10

def get_python_file_path(index):
    return os.path.join(PYTHON_FOLDER_NAME, f"{index:03}.py")

def get_go_file_path(index):
    return os.path.join(GO_FOLDER_NAME, f"{index:03}.go")

def is_file_completed(file_path):
    if not os.exists(file_path):
        return False

    with open(file_path, "r", encoding="utf-8") as file:
        file_line = file.readline()
        return file_line.startswith("# COMPLETED")

def generate_table():
    rows = math.ceil(NUMBER_OF_PROBLEMS / COLUMNS)
    lines = [
        "| "*COLUMNS+"|",
        "| --- "*COLUMNS+"|",
    ]

    current_line = ""
    for i in range(1, NUMBER_OF_PROBLEMS):
        python_file_path = get_python_file_path(i)
        
        add_link = is_file_completed()

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