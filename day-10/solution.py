"""
Solution for day 10
"""

def read_file(filename):
    ''' read the input data '''
    return [line.strip() for line in open(filename, 'r', encoding="utf-8").readlines()]

def run_part1(instructions):
    ''' Run the simulation for part 1 '''
    x = 1
    x_history = list([1])
    for instruction in instructions:
        x_history.append(x)
        if instruction.startswith('addx'):
            x += int(instruction.split()[1])
            x_history.append(x)
    return x_history

def run_part2(instructions):
    ''' Run the simulation for part 2 '''
    x = 1
    x_history = list()
    for instruction in instructions:
        x_history.append(x)
        if instruction.startswith('addx'):
            x += int(instruction.split()[1])
            x_history.append(x)

    crt_lines, crt_line, crt_pos = list(), '', 0
    for cycle in range(len(x_history)):
        # determine if we need to start a new crt line
        if (cycle) % 40 == 0:
            crt_lines.append(crt_line)
            crt_line = ''
            crt_pos = 0
        # determine what to render to the crt
        x_pos = x_history[cycle - 1] if cycle > 0 else 0
        crt_line += '#' if abs(crt_pos - x_pos) <= 1 else ' '
        crt_pos += 1
    crt_lines.append(crt_line)
    return crt_lines

# part 1
data = read_file('./day-10/input.txt')
result1 = run_part1(data)
part_1_total = 0
points_of_interest = [20, 60, 100, 140, 180, 220]
for i in points_of_interest:
    part_1_total += i * result1[i-1]
print(part_1_total) # 14920

# part 2
crts = run_part2(data)
for crt in crts:
    print(crt)
