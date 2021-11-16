import os, logging

logger = logging.getLogger("python")

class Python:

    def __init__(self, folder_path):
        self.name = "python"
        self.folder_path = folder_path

    def get_file_path(self, number):
        file_name = f"{number:03d}.py"
        file_path = os.path.join(self.folder_path, self.name, file_name)
        return file_path
        
    def create(self, problem):
        number = problem["number"]
        description = problem["description"]
        hash = problem["hash"]

        file_path = self.get_file_path(number)        
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

    def is_completed(self, number):
        file_path = self.get_file_path(number)
        if not os.path.exists(file_path):
            return False

        with open(file_path, "r", encoding="utf-8") as file:
            file_line = file.readline()
            return file_line.startswith("# COMPLETED")
