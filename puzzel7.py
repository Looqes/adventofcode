input = [line for line in open("input7").read().split("\n") if line]


class Directory:

    def __init__(self, name, parent=None):
        self.name = name
        self.contents = []
        self.size = 0
        self.parent = parent

    def add_subdir(self, dir):
        self.contents.append(dir)

    def get_dir(self, name):
        for dir in self.contents:
            if dir.name == name:
                return dir

    def print_subtree(self, level=0):
        print(('\t'* level) + self.name)
        for item in self.contents:
            item.print_subtree(level+1)

    def add_file(self, size):
        self.size += size

    def get_size(self):
        return self.size + sum([dir.get_size() for dir in self.contents])
    

# Challenge1

root = Directory("root")
current_directory = root

list_of_directories = [root]

for line in input[1:]:
    line = line.split(" ")

    # Movement or ls
    if line[0] == "$":            
        if line[1] == "cd":
            if line[2] != "..":
                current_directory = current_directory.get_dir(line[2])
            else:
                current_directory = current_directory.parent
    # Directory
    elif line[0] == "dir":
        new_Dir = Directory(line[1], current_directory)
        list_of_directories.append(new_Dir)

        if current_directory:
            current_directory.add_subdir(new_Dir)
    # File
    else:
        current_directory.add_file(int(line[0]))

# root.print_subtree()
# for file in list_of_directories:
#     print(file.name, ": ", file.get_size())

result = sum([file.get_size() for file in list_of_directories if file.get_size() <= 100000])

print("Result: ", result)


# Challenge2

free_space = 70000000 - root.get_size()

best_option = sorted([dir for dir in list_of_directories 
                      if free_space + dir.get_size() >= 30000000], 
                      key = lambda direc: direc.get_size())[0].get_size()

print(best_option)