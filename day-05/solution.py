def run_it(crate_mover_model):
    read_mode = "stacks"
    stacks_data = list()

    for line in open('input.txt', 'r').readlines():
        if line.rstrip() == '':
            # blank line at end of reading stacks
            stacks = transform(stacks_data)
            read_mode = "commands"
            continue

        if read_mode == "stacks":
            stacks_data.append(line.replace("[", " ").replace("]"," ").replace("\n", ""))

        if read_mode == "commands":
            num, from_stack, to_stack = map(int, line.replace("move ", "").replace("from ", "").replace("to ", "").split(" "))
            from_index = from_stack -1
            to_index = to_stack -1
            # do the move
            items_to_move = stacks[from_index][-num:]
            if (crate_mover_model == 9000):
                items_to_move.reverse()
            stacks[from_index] = stacks[from_index][:-num]
            stacks[to_index].extend(items_to_move)
        
    top_items = ""
    for stack in stacks:
        top_items += stack[-1:][0]
    
    return top_items

def transform(stacks_data):
    # read and remove last item (numbers row)
    stacks_numerals = stacks_data.pop()

    # create a list of stacks, each stack being a list of items
    stacks = list()
    for _ in range(len(stacks_numerals.split("   "))):
        stacks.append(list())

    stacks_data.reverse()
    
    for item in stacks_data:
        col = 0
        for char in item:
            col += 1
            if char != " ":
                colToAdd = ((col + 2)//4)-1
                stacks[colToAdd].append(char)
                
    return stacks

print(run_it(9000)) #TPGVQPFDH
print(run_it(9001)) #DMRDFRHHH