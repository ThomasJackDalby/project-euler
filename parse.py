INPUT_FILE_PATH = "problems.txt"
OUTPUT_FILE_PATH = "problems.json"

def remove_blank_lines(lines, reversed=False):
    for i in range(len(lines)):
        if lines[i] != "":
            return lines[i:]
    return []

with open(INPUT_FILE_PATH, "r", encoding="utf-8") as file:
    lines = [line.strip() for line in file.readlines()]

current_problem_number = None
current_problem_description = []
current_answer_hash = None
problems = {}
for line in lines:
    if line.startswith("Problem"):
        if current_problem_number is not None:
            current_problem_description = remove_blank_lines(current_problem_description)
            current_problem_description = remove_blank_lines(list(reversed(current_problem_description)))

            problem = {
                "number" : current_problem_number,
                "description" : current_problem_description,
                "hash" : current_answer_hash,
            }
            problems[current_problem_number] = problem

        problem_number = int(line.split()[1].strip())
        current_problem_number = problem_number
        current_problem_description = [f"Problem {current_problem_number}"]
    else:
        if current_problem_description is not None:
            current_problem_description.append(line)
            if line.strip().startswith("Answer:"):
                current_answer_hash = line.strip()[7:].strip()

import json
with open(OUTPUT_FILE_PATH, "w") as file:
    json.dump(problems, file)