import os


class FileSystemIterator:

    def __init__(self, root, only_files=False, only_dirs=False, pattern=None):
        self.root = root
        self.only_files = only_files
        self.only_dirs = only_dirs
        self.pattern = pattern
        self.generator = self.my_generator()

        if not os.path.exists(root):
            raise FileNotFoundError("The specified root directory does not exist.")

        if only_files and only_dirs:
            raise ValueError("Both 'only_files' and 'only_dirs' cannot be set to True simultaneously.")

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.generator)

    def my_generator(self):

        for root_, dirs_, files_ in os.walk(self.root):
            if self.only_files:
                for file_name in files_:
                    if self.pattern_check(file_name):
                        yield os.path.join(root_, file_name)
            elif self.only_dirs:
                for dirs_name in dirs_:
                    if self.pattern_check(dirs_name):
                        yield os.path.join(root_, dirs_name)
            else:
                for dirs_name in dirs_:
                    if self.pattern_check(dirs_name):
                        yield os.path.join(root_, dirs_name)
                for file_name in files_:
                    if self.pattern_check(file_name):
                        yield os.path.join(root_, file_name)

    def pattern_check(self, gen_object):
        if self.pattern is None or self.pattern in gen_object:
            return True
        else:
            return False

