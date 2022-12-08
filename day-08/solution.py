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

def get_trees_in_all_directions(current_row, row_idx, current_column, col_idx):
    ''' gets the trees in all 4 directions from the current tree position '''
    tr_left = current_row[0:col_idx][::-1] # [::-1] reverses the string
    tr_right = current_row[col_idx + 1:]
    tr_up = current_column[0:row_idx][::-1] # [::-1] reverses the string
    tr_down = current_column[row_idx + 1:]

    return tr_left, tr_right, tr_up, tr_down

def is_tree_visible(my_tree, tree_lists):
    ''' determines whether my tree is taller than all the trees in any of the lines '''
    for trees_in_line in tree_lists:
        if all(int(my_tree) > int(i) for i in trees_in_line):
            return True
    return False

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
        left, right, up, down = get_trees_in_all_directions(row, row_index, _columns[column_index], column_index)
        if is_tree_visible(tree, [left, right, up, down]):
            visible_count += 1

# part 1
print(visible_count) # 1543

# part 2
tree_scores = list()
for row_index, row in enumerate(_rows):
    for column_index, tree in enumerate(row):
        trees_left, trees_right, trees_up, trees_down = \
            get_trees_in_all_directions(row, row_index, _columns[column_index], column_index)

        left = distance_viewable(tree, trees_left)
        right = distance_viewable(tree, trees_right)
        up = distance_viewable(tree, trees_up)
        down = distance_viewable(tree, trees_down)

        tree_scores.append(left * right * up * down)

print(max(tree_scores)) # 595080
