""" build.py: Used to generate a set of blank project euler python files. """

import os

FILE_PATH = "problems.txt"

with open(FILE_PATH, "r", encoding="utf-8") as file:
    lines = [line.strip() for line in file.readlines()]

current_problem_number = None
current_problem_description = []
current_answer_hash = None
for line in lines:
    if line.startswith("Problem"):
        if current_problem_number is not None:
            file_path = f"{current_problem_number:03d}.py"
            if not os.path.exists(file_path):
                with open(file_path, "w", encoding="utf-8") as file:
                    header = ["\"\"\"\n"]
                    footer = [
                        "\"\"\"\n",
                        "from common import check\n",
                        "\n"
                        f"PROBLEM_NUMBER = {current_problem_number}\n",
                        f"ANSWER_HASH = \"{current_answer_hash}\"\n"
                        "\n",
                        "\n",
                        "\n",
                        "check(None, PROBLEM_NUMBER, ANSWER_HASH)\n"
                    ]
                    problem_lines = header + [f"    {line}\n" for line in current_problem_description] + footer

                    # only allow single blank lines between lines, and none first or last.
                    temp_lines = []
                    is_blank = True
                    for problem_line in problem_lines:
                        if not problem_line.strip():
                            if not is_blank:
                                temp_lines.append(problem_line)
                                is_blank = True
                        else:
                            is_blank = False
                            temp_lines.append(problem_line)
                    problem_lines = temp_lines

                    while not problem_lines[-2].strip():
                        problem_lines.pop(-2)

                    file.writelines(problem_lines)

        problem_number = int(line.split()[1].strip())
        current_problem_number = problem_number
        current_problem_description = [f"Problem {current_problem_number}"]
    else:
        if current_problem_description is not None:
            current_problem_description.append(line)
            if line.strip().startswith("Answer:"):
                current_answer_hash = line.strip()[7:].strip()