"""
Solution for day 08
"""

def read_file(filename):
    ''' read the input data '''
    return [line.strip() for line in open(filename, 'r', encoding="utf-8").readlines()]

def transform_to_columns(rows):
    ''' transforms the data from rows into columns '''
    columns = [''] * len(rows[0])
    for row in rows:
        for i, char in enumerate(row):
            columns[i] += char

    return columns

def is_tree_visible(my_tree, trees_in_line):
    ''' determines whether tree is taller than all trees in the line '''
    return all(int(my_tree) > int(i) for i in trees_in_line)

def distance_viewable(my_tree, trees_in_line):
    ''' determines how far along the line is visible from the current tree '''
    for i, tree_in_line in enumerate(trees_in_line):
        if int(tree_in_line) >= int(my_tree):
            return i + 1
    return len(trees_in_line)

_rows = read_file('./day-08/input.txt')
_columns = transform_to_columns(_rows)

visible_count = 0

for row_index, row in enumerate(_rows):
    if row_index in (0, len(_rows) - 1):
        # first and last row - all trees are visible
        visible_count += len(_rows)
        continue

    for column_index, tree in enumerate(row):
        if column_index in (0, len(row) - 1):
            # start or end of row - tree is visible
            visible_count += 1
            continue

        # This is an "inner tree"
        trees_left = row[0:column_index][::-1] # [::-1] reverses the string
        trees_right = row[column_index + 1:]
        trees_up = _columns[column_index][0:row_index] # [::-1] reverses the string
        trees_down = _columns[column_index][row_index + 1:]

        if is_tree_visible(tree, trees_left) or \
            is_tree_visible(tree, trees_right) or \
            is_tree_visible(tree, trees_up) or \
            is_tree_visible(tree, trees_down):
            visible_count += 1

# part 1
print(visible_count) # 1543

# part 2
tree_scores = list()
for row_index, row in enumerate(_rows):
    for column_index, tree in enumerate(row):
        trees_left = row[0:column_index][::-1] # [::-1] reverses the string
        trees_right = row[column_index + 1:]
        trees_up = _columns[column_index][0:row_index][::-1] # [::-1] reverses the string
        trees_down = _columns[column_index][row_index + 1:]

        left = distance_viewable(tree, trees_left)
        right = distance_viewable(tree, trees_right)
        up = distance_viewable(tree, trees_up)
        down = distance_viewable(tree, trees_down)

        tree_scores.append(left * right * up * down)

print(max(tree_scores)) # 595080
