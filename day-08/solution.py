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
tree_scores = list()

for row_index, row in enumerate(_rows):
    for column_index, tree in enumerate(row):

        # get trees in each direction
        left = row[0:column_index][::-1] # [::-1] reverses the string
        right = row[column_index + 1:]
        up = _columns[column_index][0:row_index][::-1] # [::-1] reverses the string
        down = _columns[column_index][row_index + 1:]

        # for part 1
        if is_tree_visible(tree, [left, right, up, down]):
            visible_count += 1

        # for part 2
        v_left = distance_viewable(tree, left)
        v_right = distance_viewable(tree, right)
        v_up = distance_viewable(tree, up)
        v_down = distance_viewable(tree, down)

        tree_scores.append(v_left * v_right * v_up * v_down)

# part 1
print(visible_count) # 1543

# part 2
print(max(tree_scores)) # 595080
