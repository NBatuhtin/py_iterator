from file_iterator.FileSystemIterator import FileSystemIterator


if __name__ == "__main__":
    for item in FileSystemIterator("/dir", False, False, None):
        print(item)

    print("################################")

    print(next(FileSystemIterator("/tmp", False, False, None)))