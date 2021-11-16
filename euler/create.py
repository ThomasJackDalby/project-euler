import os, json, sys, logging
from templates import templates

logger = logging.getLogger("euler")

PROBLEMS_FILE_NAME = "problems.json"
root_folder_path = os.path.dirname(__file__)
problems_folder_path = os.path.join(root_folder_path, PROBLEMS_FILE_NAME)

solutions_folder_path = os.path.join(root_folder_path, "..", "solutions")
templates = [template(solutions_folder_path) for template in templates]

if __name__ == "__main__":

    if len(sys.argv) != 3:
        raise Exception("2 arguments required. Language and problem number.")

    language = sys.argv[1]
    problem_number = sys.argv[2]

    with open(problems_folder_path, "r") as file:
        problems = json.load(file) 

    if problem_number not in problems:
        raise Exception(f"[{problem_number}] is not a valid problem number.")
    problem = problems[problem_number]

    template = next((template for template in templates if template.name == language), None)
    if template is None:
        print(f"No template for language [{language}].")
        exit()
    
    template.create(problem)
