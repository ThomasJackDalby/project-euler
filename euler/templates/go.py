import os

class Go:
    def __init__(self, folder_path):
        self.name = "go"
        self.folder_path = folder_path

    def get_file_path(self, number):
        file_name = f"{number:03d}.go"
        file_path = os.path.join(self.folder_path, self.name, file_name)
        return file_path

    def is_completed(self, number):
        file_path = self.get_file_path(number)
        if not os.path.exists(file_path):
            return False

        with open(file_path, "r", encoding="utf-8") as file:
            file_line = file.readline()
            return file_line.startswith("# COMPLETED")
