rock='A'
paper='B'
scissors='C'

lose=0
draw=3
win=6

mappings = [[rock,rock,draw],[rock,paper,win],[rock,scissors,lose],[paper,rock,lose],[paper,paper,draw],[paper,scissors,win],[scissors,rock,win],[scissors,paper,lose],[scissors,scissors,draw]]

def translate_xyz_to_rps(xyz):
    return rock if xyz == 'X' else paper if xyz == 'Y' else scissors

def translate_xyz_to_required_outcome(xyz):
    return lose if xyz == 'X' else draw if xyz == 'Y' else win

def score_response(response):
    return 1 if response == rock else 2 if response == paper else 3

def play(challenge, response):
    for mapping in mappings:
        if challenge == mapping[0] and response == mapping[1]:
            return mapping[2]

def how_to_get(required_outcome, challenge):
    for mapping in mappings:
        if challenge == mapping[0] and required_outcome == mapping[2]:
            return mapping[1]

def score_part1_round(challenge, response):
    return score_response(response) + play(challenge, response)

def score_part2_round(challenge, required_outcome):
    required_response = how_to_get(required_outcome, challenge)
    return score_response(required_response) + required_outcome

lines = open('input.txt', 'r').readlines()

score_part_1 = 0
score_part_2 = 0

for line in lines:
    vals = line.split()
    score_part_1 += score_part1_round(vals[0], translate_xyz_to_rps(vals[1]))

    score_part_2 += score_part2_round(vals[0], translate_xyz_to_required_outcome(vals[1]))

print(score_part_1)
print(score_part_2)