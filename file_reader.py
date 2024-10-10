import os


class FileReader:
    def __init__(self, dir: str):
        self.dir = dir

    def read(self):
        files = []

        for path, _, file_list in os.walk(self.dir):
            for file_name in file_list:
                file_path = os.path.join(path, file_name)
                print("start read file:", file_path)
                files.append(file_path)

        return files
