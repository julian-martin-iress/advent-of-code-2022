"""
Solution for day 04
"""

lines = open('./day-04/input.txt', 'r', encoding="utf-8").readlines()

score_part_1, score_part_2 = 0, 0

for line in lines:
    start1, end1, start2, end2 = map(int, line.replace(",", "-").split("-"))
    score_part_1 += 1 if (start1 <= start2 and end1 >= end2 ) or \
                        (start2 <= start1 and end2 >= end1) else 0
    score_part_2 += 0 if (end1 < start2 ) or (end2 < start1) else 1

print(score_part_1, score_part_2)
