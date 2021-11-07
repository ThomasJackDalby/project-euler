import os, json, sys, logging
logger = logging.getLogger("euler")

PROBLEMS_FILE_PATH = "problems.json"
root_folder_path = os.path.dirname(__file__)

def python(problem):
    number = problem["number"]
    description = problem["description"]
    hash = problem["hash"]

    file_name = f"{number:03d}.py"
    file_path = os.path.join(root_folder_path, "python", file_name)

    if os.path.exists(file_path):
        logger.warning(f"[{file_path}] already exists")
        return

    header = ["\"\"\"\n"]
    footer = [
        "\"\"\"\n",
        "from common import check\n",
        "\n"
        f"PROBLEM_NUMBER = {number}\n",
        f"ANSWER_HASH = \"{hash}\"\n"
        "\n",
        "\n",
        "\n",
        "check(None, PROBLEM_NUMBER, ANSWER_HASH)\n"
    ]
    problem_lines = header + [f"    {line}\n" for line in description] + footer

    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(problem_lines)

def go(problem):
    print("Go ...")

if __name__ == "__main__":

    if len(sys.argv) != 3:
        raise Exception("2 arguments required. Language and problem number.")

    language = sys.argv[1]
    problem_number = sys.argv[2]

    with open(PROBLEMS_FILE_PATH, "r") as file:
        problems = json.load(file) 

    if problem_number not in problems:
        raise Exception(f"[{problem_number}] is not a valid problem number.")
    problem = problems[problem_number]

    create_template = getattr(sys.modules[__name__], language)
    
    create_template(problem)
