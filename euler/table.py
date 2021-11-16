"""table.py"""

import math, os, logging
from templates import templates

NUMBER_OF_PROBLEMS = 500
COLUMNS = 10

logger = logging.getLogger("table")
local_folder_path = os.path.dirname(__file__)
repo_folder_path = os.path.join(local_folder_path, "..")
solutions_folder_path = os.path.join(repo_folder_path, "solutions")

templates = [template(solutions_folder_path) for template in templates]

def generate_table():
    rows = math.ceil(NUMBER_OF_PROBLEMS / COLUMNS)
    lines = [
        "| "*COLUMNS+"|\n",
        "| --- "*COLUMNS+"|\n",
    ]

    current_line = ""
    for i in range(1, NUMBER_OF_PROBLEMS):
        
        links = []
        for language in templates:
            file_path = language.get_file_path(i)
            if os.path.exists(file_path):
                rel_path = os.path.relpath(file_path, repo_folder_path).replace("\\", "/")
                links.append((language.name, rel_path, language.is_completed(i)))
            else:
                links.append((None, None, None))
            
        cell = f"| {i:03d} "
        if len(links) > 0:
            links = "<br>".join((f"[{language}]({file_path})" if not is_completed else f"**[{language}]({file_path})**") if language is not None else "." for (language, file_path, is_completed) in links)
            cell += f"<br>{links} "

        current_line += cell
        if i % COLUMNS == 0:
            current_line += "|\n"
            lines.append(current_line)
            current_line = ""

    with open("README.md", "r") as file:
        readme_lines = file.readlines()

    def find_line(text):
        for line_number, line in enumerate(readme_lines):
            if line.startswith(text):
                return line_number
        return None

    line_number = find_line("## Progress")
    if line_number is None:
        raise Exception()

    prefix_lines = readme_lines[:line_number+2]

    with open("README.md", "w") as file:
        file.writelines(prefix_lines + lines)

if __name__ == "__main__":
    generate_table()