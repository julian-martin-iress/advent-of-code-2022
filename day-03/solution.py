"""
Solution for day 03
"""

import string

alphabet_mapping = list(string.ascii_letters)

def score_for(char):
    return alphabet_mapping.index(char) + 1

lines = open('./day-03/input.txt', 'r', encoding="utf-8").readlines()

score_part_1 = 0

for line in lines:
    firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
    for char in firstpart:
        if char in secondpart:
            score_part_1 += score_for(char)
            break

print(score_part_1)

# part 2
score_part_2 = 0
i = 0

while i < len(lines):
    rucksack1 = lines[i]
    rucksack2 = lines[i + 1]
    rucksack3 = lines[i + 2]

    for char in rucksack1:
        if char in rucksack2 and char in rucksack3: 
            score_part_2 += score_for(char)
            break

    i += 3

print(score_part_2)
