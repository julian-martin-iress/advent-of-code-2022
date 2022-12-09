"""
Solution for day 09
"""

class Knot:
    ''' Defines a knot's location '''
    x: int = 0
    y: int = 0

def read_file(filename):
    ''' read the input data '''
    return [line.strip() for line in open(filename, 'r', encoding="utf-8").readlines()]

def run_simulation(instructions, num_of_knots):
    ''' Run the simulation '''
    knots = [Knot() for _ in range(num_of_knots)]
    head = knots[0]
    tail = knots[num_of_knots - 1]

    tail_locations = set()
    tail_locations.add(f"{tail.x},{tail.y}")

    for line in instructions:
        direction, times = line.split()
        for _ in range(int(times)):
            # Move the head
            if direction == 'R': head.x += 1
            if direction == 'L': head.x -= 1
            if direction == 'U': head.y += 1
            if direction == 'D': head.y -= 1

            for i, knot in enumerate(knots):
                if (knot == head): continue
                # Check if this knot should move
                knot_in_front = knots[i-1]
                if abs(knot_in_front.x - knot.x) > 1 or abs(knot_in_front.y - knot.y) > 1:
                    # Move this knot
                    if knot_in_front.x != knot.x:
                        knot.x += 1 if knot_in_front.x > knot.x else -1
                    if knot_in_front.y != knot.y:
                        knot.y += 1 if knot_in_front.y > knot.y else -1
                    # Store current tail location
                    tail_locations.add(f"{tail.x},{tail.y}")

    return len(tail_locations)

lines = read_file('./day-09/input.txt')

# part 1
print(run_simulation(lines, 2)) # 6026

# part 2
print(run_simulation(lines, 10)) # 2273
