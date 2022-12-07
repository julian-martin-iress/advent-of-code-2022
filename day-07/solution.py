"""
Solution for day 07
"""

def build_folders_and_files():
    ''' Build sets for all folder and files '''
    lines = open('./day-07/input.txt', 'r', encoding="utf-8").readlines()

    folders_set, files_set = set(), set()

    current_path = ''

    for line in lines:
        line = line.rstrip()
        if line == "$ cd ..":
            current_path = current_path[:current_path.rfind("/")]
            continue
        if line.startswith('$ cd '):
            current_path += '/' + line[5:]
            folders_set.add(current_path)
            continue
        if line.startswith('$ ls') or line.startswith('dir'):
            continue

        # if we get here, it's a file
        file_size, file_name = line.split()
        files_set.add(current_path + '/' + file_name + ':' + file_size)

    return folders_set, files_set

all_sizes = list()
part_1_total = 0

folders, files = build_folders_and_files()
for folder in folders:
    folder_size = 0
    for file in files:
        if folder in file:
            # This file is in the folder
            filename, size = file.split(':')
            folder_size += int(size)

    all_sizes.append(folder_size)
    if folder_size <= 100000:
        part_1_total += folder_size

all_sizes.sort()
root_folder_size = all_sizes.pop()

additional_space_required = root_folder_size - 40000000
size_of_folder_to_delete = next(size for size in all_sizes if size >= additional_space_required)

print(part_1_total) # 1844187
print(size_of_folder_to_delete) # 4978279
