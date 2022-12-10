"""
Solution for day 10
"""

def read_file(filename):
    ''' read the input data '''
    return [line.strip() for line in open(filename, 'r', encoding="utf-8").readlines()]

def run_simulation(instructions):
    ''' Run the simulation '''
    x = 1
    x_history = list()#list([x])
    for instruction in instructions:
        x_history.append(x)
        if instruction.startswith('addx'):
            x += int(instruction.split()[1])
            x_history.append(x)

    # for part 2
    crt_lines = list()
    crt_line = ''
    crt_pos = 0
    for cycle in range(len(x_history)):
        # if cycle == 0:
        #     continue
        
        # determine if we need to start a new crt line
        if (cycle) % 40 == 0:
            crt_lines.append(crt_line)
            crt_line = ''
            crt_pos = 0
        # determine what to render to the crt
        x_pos = x_history[cycle - 1]
        if crt_pos == x_pos or crt_pos == x_pos + 1 or crt_pos == x_pos - 1:
            crt_line += '#'
        else:
            crt_line += ' '
        crt_pos += 1
    crt_lines.append(crt_line)
    return x_history, crt_lines

# part 1
data = read_file('./day-10/input.txt')
result, crts = run_simulation(data)
part_1_total = 0
points_of_interest = [20, 60, 100, 140, 180, 220]
for i in points_of_interest:
    part_1_total += i * result[i-1]
print(part_1_total) # 14920 (test 13140)

# part 2
for crt in crts:
    print(crt)
    