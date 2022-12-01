lines = open('Input.txt', 'r').readlines()

totals = list()
currentTotal = 0
for line in lines:
    if line.rstrip() != '':
        currentTotal = currentTotal + int(line)
    else:
        totals.append(currentTotal)
        currentTotal = 0

# Part 1 answer
print(max(totals))

# Part 2 answer
totals.sort(reverse=True)
print(sum(totals[0:3]))