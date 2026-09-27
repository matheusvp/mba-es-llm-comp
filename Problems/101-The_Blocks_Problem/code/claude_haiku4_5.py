def find_block(stacks, block):
    for pos, stack in enumerate(stacks):
        if block in stack:
            return pos, stack.index(block)
    return None, None

def are_in_same_stack(stacks, a, b):
    for stack in stacks:
        if a in stack and b in stack:
            return True
    return False

def return_to_initial(stacks, block):
    pos, idx = find_block(stacks, block)
    if pos is not None:
        pile = stacks[pos][idx:]
        stacks[pos] = stacks[pos][:idx]
        stacks[block] = pile

def move_onto(stacks, a, b):
    if a == b or are_in_same_stack(stacks, a, b):
        return
    pos_a, idx_a = find_block(stacks, a)
    pos_b, idx_b = find_block(stacks, b)
    for block in stacks[pos_a][idx_a+1:]:
        return_to_initial(stacks, block)
    stacks[pos_a] = stacks[pos_a][:idx_a]
    pos_b, idx_b = find_block(stacks, b)
    for block in stacks[pos_b][idx_b+1:]:
        return_to_initial(stacks, block)
    pos_b, idx_b = find_block(stacks, b)
    stacks[pos_b].append(a)

def move_over(stacks, a, b):
    if a == b or are_in_same_stack(stacks, a, b):
        return
    pos_a, idx_a = find_block(stacks, a)
    pos_b, idx_b = find_block(stacks, b)
    for block in stacks[pos_a][idx_a+1:]:
        return_to_initial(stacks, block)
    stacks[pos_a] = stacks[pos_a][:idx_a]
    pos_b, idx_b = find_block(stacks, b)
    stacks[pos_b].append(a)

def pile_onto(stacks, a, b):
    if a == b or are_in_same_stack(stacks, a, b):
        return
    pos_a, idx_a = find_block(stacks, a)
    pos_b, idx_b = find_block(stacks, b)
    pile = stacks[pos_a][idx_a:]
    stacks[pos_a] = stacks[pos_a][:idx_a]
    pos_b, idx_b = find_block(stacks, b)
    for block in stacks[pos_b][idx_b+1:]:
        return_to_initial(stacks, block)
    pos_b, idx_b = find_block(stacks, b)
    stacks[pos_b].extend(pile)

def pile_over(stacks, a, b):
    if a == b or are_in_same_stack(stacks, a, b):
        return
    pos_a, idx_a = find_block(stacks, a)
    pos_b, idx_b = find_block(stacks, b)
    pile = stacks[pos_a][idx_a:]
    stacks[pos_a] = stacks[pos_a][:idx_a]
    pos_b, idx_b = find_block(stacks, b)
    stacks[pos_b].extend(pile)

n = int(input())
stacks = [[i] for i in range(n)]

while True:
    tokens = input().split()
    if tokens[0] == 'quit':
        break
    action = tokens[0]
    a = int(tokens[1])
    relation = tokens[2]
    b = int(tokens[3])
    if action == 'move':
        if relation == 'onto':
            move_onto(stacks, a, b)
        else:
            move_over(stacks, a, b)
    else:
        if relation == 'onto':
            pile_onto(stacks, a, b)
        else:
            pile_over(stacks, a, b)

for i in range(n):
    if stacks[i]:
        print(f"{i}: {' '.join(map(str, stacks[i]))}")
    else:
        print(f"{i}:")