import os
import pickle
from datetime import datetime


class Block:
    def __init__(self):
        self.block_size = 1024
        self.data = bytearray(self.block_size)

    def write(self, data: bytearray):
        self.data = data

    def read(self) -> bytearray:
        return self.data


class Inode:
    def __init__(self):
        self.file_size = 0
        self.file_blocks_index = []
        self.ctime = datetime.now()
        self.mtime = datetime.now()
        self.atime = datetime.now()

    def add_block(self, block_index: int):
        self.file_blocks_index.append(block_index)

    def remove_block(self, block_index: int):
        self.file_blocks_index.remove(block_index)


class FileSystem:
    def __init__(self):
        self.root = Directory("/", None)
        self.current_directory = self.root
        self.file_block_nums = 2560
        self.valid_blocks = bytearray(self.file_block_nums)
        self.space = [Block() for _ in range(self.file_block_nums)]

    def create_file(self, name):
        for file in self.current_directory.files:
            if file.name == name:
                print("File already exists")
                return False
        file = File(name)
        self.current_directory.add_file(file)
        return True

    def delete_file(self, name):
        file = self.current_directory.get_file(name)
        if file:
            file.clear(self)
            self.current_directory.remove_file(file)
            return True
        else:
            print("File not found")
            return False

    def read_file(self, name):
        file = self.current_directory.get_file(name)
        if file:
            return file.read(self)
        else:
            return bytearray()

    def write_file(self, name, data):
        file = self.current_directory.get_file(name)
        if file:
            if file.write(data, self):
                return True
            else:
                return False
        else:
            return False

    def list_directory(self):
        return self.current_directory.list_contents()

    def change_directory(self, name):
        if name == "..":
            parent = self.current_directory.parent
            if parent:
                self.current_directory = parent
            return
        for dir in self.current_directory.subdirectories:
            if dir.name == name:
                self.current_directory = dir
                return
        directory = self.find_directory(self.root, name)
        if directory:
            self.current_directory = directory

    def find_directory(self, directory, name):
        if directory.name == name:
            return directory

        for subdirectory in directory.subdirectories:
            result = self.find_directory(subdirectory, name)
            if result:
                return result

        return None

    def make_directory(self, name):
        for dir in self.current_directory.subdirectories:
            if dir.name == name:
                print("Directory already exists")
                return False
        directory = Directory(name, self.current_directory)
        self.current_directory.add_subdirectory(directory)
        return True

    def remove_directory(self, name):
        for subdirectory in self.current_directory.subdirectories:
            if name == subdirectory.name:
                self.current_directory.remove_subdirectory(subdirectory)
                return True
        directory = self.find_directory(self.root, name)
        parent = directory.parent
        if directory:
            parent.remove_subdirectory(directory)
            return True
        else:
            print("Directory not found")
            return False

    def save_to_disk(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    def get_current_path(self):
        # 获取当前目录的路径
        if self.current_directory.name == "/":
            return "/"
        path = ""
        directory = self.current_directory
        while directory.name != "/":
            path = "/"+directory.name + path
            directory = directory.parent
        return path

    def get_file_size(self, file):
        return file.inode.file_size

    def get_file_mtime(self, file):
        return file.inode.mtime

    def get_dir_item_nums(self, directory):
        return len(directory.files) + len(directory.subdirectories)

    def rename_file(self, old_name, new_name):
        """重命名文件
        Returns:
            bool: 是否成功
            int: 错误码, 0表示成功, 1表示文件不存在, 2表示新文件名与旧文件名相同, 3表示新文件名已存在, 4表示新文件名为空
        """
        if new_name is None:
            return False, 4
        if new_name == old_name:
            return False, 2
        for file in self.current_directory.files:
            if file.name == new_name:
                return False, 3
        file = self.current_directory.get_file(old_name)
        if file:
            file.name = new_name
            return True, 0
        else:
            return False, 1

    def rename_directory(self, old_name, new_name):
        """重命名目录
        Returns:
            bool: 是否成功
            int: 错误码, 0表示成功, 1表示目录不存在, 2表示新目录名与旧目录名相同, 3表示新目录名已存在, 4表示新目录名为空
        """
        if new_name is None:
            return False, 4
        if new_name == old_name:
            return False, 2
        if new_name in [dir.name for dir in self.current_directory.subdirectories]:
            return False, 3
        directory = self.current_directory.get_subdirectory(old_name)
        if directory:
            directory.name = new_name
            return True, 0
        else:
            return False, 1


class File:
    def __init__(self, name):
        self.name = name
        self.inode = Inode()
        self.type = "file"

    def read(self, fs: FileSystem) -> bytearray:
        data = bytearray()
        self.inode.atime = datetime.now()
        for block_index in self.inode.file_blocks_index:
            data += fs.space[block_index].read()
        return data

    def write(self, data: bytearray, fs: FileSystem) -> bool:
        self.clear(fs)
        self.inode.file_size = len(data)
        block_count = len(data) // 1024 + 1
        for i in range(block_count):
            j = 0
            for j in range(fs.file_block_nums):
                if fs.valid_blocks[j] == 0:
                    fs.valid_blocks[j] = 1
                    block = fs.space[j]
                    if i == 0:
                        self.inode.mtime = datetime.now()
                        self.inode.atime = datetime.now()
                    block.write(data[i * 1024: min((i + 1) * 1024, len(data))])
                    self.inode.add_block(j)
                    break
            if j == fs.file_block_nums-1:
                print("No more space available")
                return False
        return True

    def clear(self, fs: FileSystem):
        """释放文件占用block
        """
        self.inode.ctime = datetime.now()
        self.inode.mtime = datetime.now()
        self.inode.atime = datetime.now()
        for i in self.inode.file_blocks_index:
            fs.valid_blocks[i] = 0
        self.inode.file_blocks_index = []


class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.files = []
        self.subdirectories = []
        self.type = "directory"

    def add_file(self, file):
        self.files.append(file)

    def remove_file(self, file):
        self.files.remove(file)

    def get_file(self, name):
        for file in self.files:
            if file.name == name:
                return file

    def add_subdirectory(self, directory):
        self.subdirectories.append(directory)

    def remove_subdirectory(self, directory):
        if directory in self.subdirectories:
            for file in directory.files:
                directory.remove_file(file)
            self.subdirectories.remove(directory)
            directory.parent = None
            directory.remove_all_subdirectories()

    def remove_all_subdirectories(self):
        for directory in self.subdirectories:
            for file in directory.files:
                directory.remove_file(file)
            self.subdirectories.remove(directory)
            directory.parent = None
            directory.remove_all_subdirectories()

    def get_subdirectory(self, name):
        for directory in self.subdirectories:
            if directory.name == name:
                return directory

    def list_contents(self):
        dir_contents = []
        file_contents = []
        for directory in self.subdirectories:
            dir_contents.append(directory)
        for file in self.files:
            file_contents.append(file)
        return dir_contents, file_contents


def load_from_disk(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)


if __name__ == '__main__':
    if os.path.exists("fs.pickle"):
        fs = load_from_disk("fs.pickle")
    else:
        fs = FileSystem()
    while True:
        print(f"{fs.current_directory.name}>", end="")
        command = input()
        command_list = command.split()
        if command_list[0] == "touch":
            fs.create_file(command_list[1])
            print("file created\n")
        elif command_list[0] == "edit":
            if len(command_list) < 3:
                print("Usage: edit <filename> <data>")
                continue
            if fs.write_file(command_list[1], bytearray(command_list[2], "utf-8")):
                print("File written\n")
            else:
                print("File not found\n")
        elif command_list[0] == "cat":
            data = fs.read_file(command_list[1])
            if data:
                print(data.decode("utf-8"))
                print()
            else:
                print("File not found")
                print()
        elif command_list[0] == "rm":
            if fs.delete_file(command_list[1]):
                print("File deleted")
                print()
            else:
                print("File not found")
                print()
        elif command_list[0] == "ls":
            dir_content, file_content = fs.list_directory()
            print(
                f"Dir:{fs.current_directory.name},Total {len(dir_content)+len(file_content)}\n")
            print("Directory:")
            for item in dir_content:
                print(item.name+"/")
            print()
            print("File:")
            for item in file_content:
                print(item.name+"\t\t" +
                      f"{item.inode.file_size} bytes\t\t{item.inode.mtime}")
            print()
        elif command_list[0] == "cd":
            fs.change_directory(command_list[1])
        elif command_list[0] == "mkdir":
            fs.make_directory(command_list[1])
        elif command_list[0] == "rmdir":
            fs.remove_directory(command_list[1])
        elif command_list[0] == "exit":
            break

    fs.save_to_disk("fs.pickle")
