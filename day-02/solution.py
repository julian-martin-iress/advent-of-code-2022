"""
Solution for day 02
"""

rock, paper, scissors = 'A', 'B', 'C'
lose, draw, win = 0, 3, 6
gesture_scores = {rock: 1, paper: 2, scissors: 3}
this_beats_that = [[rock, scissors], [scissors, paper], [paper, rock]]

part1_gesture_map = {'X': rock, 'Y': paper, 'Z': scissors }
part2_outcome_map = {'X': lose, 'Y': draw, 'Z': win }

def play(their_gesture, my_gesture):
    if their_gesture == my_gesture:
        return draw
    return win if [my_gesture, their_gesture] in this_beats_that else lose

def how_to_get(outcome, their_gesture):
    if outcome == draw:
        return their_gesture
    
    i, j = (0, 1) if outcome == win else (1, 0)
    return next(gesture[i] for gesture in this_beats_that if gesture[j] == their_gesture)

def score_part1_round(their_gesture, my_gesture):
    return gesture_scores[my_gesture] + play(their_gesture, my_gesture)

def score_part2_round(their_gesture, outcome):
    my_gesture = how_to_get(outcome, their_gesture)
    return gesture_scores[my_gesture] + outcome

lines = open('./day-02/input.txt', 'r', encoding="utf-8").readlines()

score_part_1 = 0
score_part_2 = 0

for line in lines:
    their_gesture, xyz = line.split()
    score_part_1 += score_part1_round(their_gesture, part1_gesture_map[xyz])
    score_part_2 += score_part2_round(their_gesture, part2_outcome_map[xyz])

print(score_part_1) # 13268
print(score_part_2) # 15508
