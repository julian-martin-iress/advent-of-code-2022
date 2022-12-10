"""
Solution for day 10
"""

def read_file(filename):
    ''' read the input data '''
    return [line.strip() for line in open(filename, 'r', encoding="utf-8").readlines()]

def run_simulation(instructions):
    ''' Run the simulation '''
    x = 1
    x_history = list([x])

    for instruction in instructions:
        x_history.append(x)
        if instruction.startswith('addx'):
            x += int(instruction.split()[1])
            x_history.append(x)
    return x_history

# part 1
data = read_file('./day-10/input.txt')
result = run_simulation(data)
part_1_total = 0
points_of_interest = [20, 60, 100, 140, 180, 220]
for i in points_of_interest:
    part_1_total += i * result[i-1]
print(part_1_total) # 14920 (test 13140)