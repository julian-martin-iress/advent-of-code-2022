def group_contains(start1, end1, start2, end2):
    return 1 if (start1 <= start2 and end1 >= end2 ) or (start2 <= start1 and end2 >= end1) else 0

def any_overlap(start1, end1, start2, end2):
    return 0 if (end1 < start2 ) or (end2 < start1) else 1

lines = open('input.txt', 'r').readlines()

score_part_1 = 0
score_part_2 = 0

for line in lines:
    a,b,c,d= map(int, line.replace(",", "-").split("-"))
    score_part_1 += group_contains(a,b,c,d)
    score_part_2 += any_overlap(a,b,c,d)

print(score_part_1)
print(score_part_2)