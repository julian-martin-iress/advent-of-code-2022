"""
Solution for day 07
"""

def build_folders_and_files():
    ''' Build sets for all folder and files '''
    lines = open('./day-07/input.txt', 'r', encoding="utf-8").readlines()

    folders = set()
    files = set()

    current_path = ''

    for line in lines:
        line = line.rstrip()
        if line == "$ cd ..":
            current_path = current_path[:current_path.rfind("/")]
            continue
        if line.startswith('$ cd '):
            new_folder = line[5:]
            current_path += '/' + new_folder
            folders.add(current_path)
            continue
        if line.startswith('$ ls') or line.startswith('dir'):
            continue

        #if we get here, it's a file
        size, filename = line.split()
        files.add(current_path + '/' + filename + ':' + size)

    return folders, files

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


print(folders, files)
print(part_1_total) # 1844187
