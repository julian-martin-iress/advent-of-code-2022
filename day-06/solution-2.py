"""
Solution for day 06 - inspired by Steve's !!
"""

def run_it(marker_size: int):
    ''' Run the device '''
    line = open('./day-06/input.txt', 'r', encoding="utf-8").readline()

    for pos in range(0, len(line)):
        if pos + marker_size <= len(line):
            chunk_to_check = set(line[pos:pos + marker_size])
            if len(chunk_to_check) == marker_size:
                return pos + marker_size

    raise Exception("No solution was found")

print(run_it(4)) # 1909
print(run_it(14)) # 3380
