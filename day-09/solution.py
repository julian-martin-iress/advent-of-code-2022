"""
Solution for day 09
"""

def read_file(filename):
    ''' read the input data '''
    return [line.strip() for line in open(filename, 'r', encoding="utf-8").readlines()]


instructions = read_file('./day-09/input.txt')

head_x, tail_x, head_y, tail_y = 0, 0, 0, 0
tail_locations = set()
tail_locations.add(f"{tail_x},{tail_y}")

for line in instructions:
    direction, times = line.split()
    for _ in range(int(times)):
        # Move the head
        if direction == 'R': head_x += 1
        if direction == 'L': head_x -= 1
        if direction == 'U': head_y += 1
        if direction == 'D': head_y -= 1

        # Check if Tail should move
        if abs(head_x - tail_x) > 1 or abs(head_y - tail_y) > 1:
            # Move tail
            if head_x != tail_x:
                tail_x += 1 if head_x > tail_x else -1
            if head_y != tail_y:
                tail_y += 1 if head_y > tail_y else -1
            # Store new tail location
            tail_locations.add(f"{tail_x},{tail_y}")

# part 1
print(len(tail_locations)) # 6026
