def run_it(crate_mover_model):
    mode = "stacks"
    stacks_data = list()

    for line in open('input.txt', 'r').readlines():
        if line.rstrip() == '':
            # end of reading stacks
            mode = "commands"
            stacks = transform(stacks_data)
            continue

        if mode == "stacks":
            stacks_data.append(line.replace("[", " ").replace("]"," ").replace("\n", ""))

        if mode == "commands":
            how_many, from_stack, to_stack = map(int, line.replace("move ", "").replace("from ", "").replace("to ", "").split(" "))
            # do the move
            item_to_move = stacks[from_stack-1][-how_many:]
            if (crate_mover_model == 9000):
                item_to_move.reverse()
            stacks[from_stack-1] = stacks[from_stack-1][:-how_many]
            stacks[to_stack-1].extend(item_to_move)
        
    top_items = ""
    for stack in stacks:
        top_items += stack[-1:][0]
    
    return top_items

def transform(stacks_data):
    # remove last item (numbers row)
    stacks_data.pop()
    # build a list for each stack
    stacks_data.reverse()
    stacks = list()
    for x in range(9):
        stacks.append(list())
    
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