"""
Solution for day 01
"""

lines = open('./day-01/input.txt', 'r', encoding="utf-8").readlines()

totals = list()
current_total = 0
for line in lines:
    if line.rstrip() != '':
        current_total += int(line)
    else:
        totals.append(current_total)
        current_total = 0

# Part 1 answer
print(max(totals))

# Part 2 answer
totals.sort(reverse=True)
print(sum(totals[0:3]))
