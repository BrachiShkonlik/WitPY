import sys
import os
import shutil


class FileHandler:
    base_path = None
    working_directory = None

    # def get_base_path(self):
    #     current_directory = os.getcwd()
    #     while current_directory != '/':
    #         self.base_path = os.path.join(current_directory, '.wit')
    #         if os.path.isdir(self.base_path):
    #             return self.base_path
    #         current_directory = os.path.dirname(current_directory)
    #     raise FileNotFoundError(".wit directory not found.")

    @staticmethod
    def create_dir(path):
        os.mkdir(path)

    @classmethod
    def find_base_path(cls):
        current_directory = os.getcwd()
        while current_directory != '/':
            cls.base_path = os.path.join(current_directory, '.wit')
            if os.path.isdir(cls.base_path):
                return cls.base_path
            current_directory = os.path.dirname(current_directory)
        raise FileNotFoundError(".wit directory not found.")

    @classmethod
    def validate_path(cls, path):
        full_path = os.path.join(cls.working_directory, path)
        if not os.path.exists(full_path):
            raise Exception("the file dose not exists")
        return full_path

    @classmethod
    def copy_item(cls, origin, target):
        shutil.copy(origin, target)


class Wit:

    @staticmethod
    def validate_is_wit_repo():
        return FileHandler.find_base_path()

    @staticmethod
    def init():
        if Wit.validate_is_wit_repo():
            raise Exception("you have wit directory")
        else:
            FileHandler.create_dir(".wit")
            FileHandler.create_dir(".wit/images")
            FileHandler.create_dir(".wit/staging_area")

    @staticmethod
    def move_to_staging(full_path):
        target_path = os.path.join(FileHandler.base_path, "staging_area")
        FileHandler.copy_item(full_path, target_path)

    @staticmethod
    def add(args):
        full_path = FileHandler.validate_path(args[0])
        Wit.move_to_staging(full_path)

    @staticmethod
    def commit():
        pass


class WitInterface:
    @staticmethod
    def handle_commands(command, args):
        match command:
            case "init":
                Wit.init()
            case "add":
                Wit.add(args)
            case "commit":
                Wit.commit()
            case _:
                raise Exception("Sorry, your request wrong")


if __name__ == "__main__":
    # TODO: handle edge cases
    command = sys.argv[1]
    args = sys.argv[2:]
    WitInterface.handle_commands(command, args)
