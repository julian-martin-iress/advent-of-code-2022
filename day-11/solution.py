"""
Solution for day 11
"""
from math import lcm
from check import check_answer

def read_file(filename):
    ''' read the input data '''
    return [line.strip() for line in open(filename, 'r', encoding="utf-8").readlines()]

def parse_monkeys(lines):
    ''' create monkeys from input '''
    monkeys = list()
    for line in lines:
        if line.startswith('Monkey'):
            monkey = Monkey(int(line[-2]))
            monkeys.append(monkey)
        if line.startswith('Starting items:'):
            monkey.items = [int(item) for item in line.replace('Starting items:', '').replace(' ', '').split(',')]
        if line.startswith('Operation:'):
            monkey.operation_operator, monkey.operation_value = \
                line.replace('Operation: new = old ', '').split()
        if line.startswith('Test:'):
            monkey.test = int(line.split()[-1])
        if line.startswith('If true:'):
            monkey.true_result = int(line.split()[-1])
        if line.startswith('If false:'):
            monkey.false_result = int(line.split()[-1])

    return monkeys

class Monkey:
    ''' defines a monkey '''
    index: int
    items: list()
    operation_operator: str
    operation_value: str
    test: int
    true_result: int
    false_result: int
    inspect_count: int = 0

    def __str__(self):
        return f"{self.index}({self.items} - inspect_count: {self.inspect_count})"

    def __init__(self, index):
        self.index = index

    def do_turn(self, all_monkeys, worry_factor, modulus):
        ''' monkey takes a turn to process all their items '''
        for item in self.items:

            self.inspect_count += 1

            # do the operation on the item
            if self.operation_operator == '+':
                item += int(self.operation_value)
            elif self.operation_value == 'old':
                item *= item
            else: item *= int(self.operation_value)

            # divide item by worry_factor - part 1
            item = item // int(worry_factor)
            # reduce item by modulo operation - part 2
            if modulus > 0:
                item = item % modulus

            # throw the item!
            target_monkey = self.true_result if item % int(self.test) == 0 else self.false_result
            all_monkeys[target_monkey].items.append(item)
        self.items = list()

data = read_file('./day-11/input.txt')

# part 1
monkeys = parse_monkeys(data)
for _ in range(20):
    for m in monkeys:
        m.do_turn(monkeys, 3, 0)

monkeys.sort(key=lambda x: x.inspect_count, reverse=True)

part_1_total = monkeys[0].inspect_count * monkeys[1].inspect_count
check_answer(part_1_total, 61503) # real: 61503 test: 10605


# part 2
monkeys = parse_monkeys(data)
modulus = lcm(*(monkey.test for monkey in monkeys))
for r in range(10000):
    for m in monkeys:
        m.do_turn(monkeys, 1, modulus)

monkeys.sort(key=lambda x: x.inspect_count, reverse=True)

part_2_total = monkeys[0].inspect_count * monkeys[1].inspect_count
check_answer(part_2_total, 14081365540) # real: 14081365540 test: 2713310158