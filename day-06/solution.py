"""
Solution for day 06
"""

def run_it(marker_size: int):
    ''' Run the device '''
    line = open('./day-06/input.txt', 'r', encoding="utf-8").readline()

    pos = 0
    for _ in line:
        if pos + marker_size <= len(line):
            dupe_found = False
            chunk_to_check = line[pos:pos + marker_size]
            for char in chunk_to_check:
                if chunk_to_check.count(char) > 1:
                    dupe_found = True
                    break
            if dupe_found is False:
                return pos + marker_size
            pos += 1

    raise Exception("No solution was found")

print(run_it(4)) # 1909
print(run_it(14)) # 3380
