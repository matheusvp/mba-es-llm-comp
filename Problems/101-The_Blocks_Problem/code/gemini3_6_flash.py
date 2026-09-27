import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    
    # Each position i holds a list representing the stack of blocks
    stacks = [[i] for i in range(n)]
    # Maps block number to its current (position, height_index)
    pos = {i: (i, 0) for i in range(n)}

    def clear_above(a):
        p, idx = pos[a]
        while len(stacks[p]) > idx + 1:
            top_block = stacks[p].pop()
            stacks[top_block].append(top_block)
            pos[top_block] = (top_block, 0)

    ptr = 1
    while ptr < len(input_data):
        cmd1 = input_data[ptr]
        if cmd1 == 'quit':
            break

        a = int(input_data[ptr + 1])
        cmd2 = input_data[ptr + 2]
        b = int(input_data[ptr + 3])
        ptr += 4

        # Ignore illegal commands
        pos_a, idx_a = pos[a]
        pos_b, idx_b = pos[b]
        if a == b or pos_a == pos_b:
            continue

        if cmd1 == 'move':
            clear_above(a)
        if cmd2 == 'onto':
            clear_above(b)

        # Move block 'a' and all blocks above it to block 'b''s stack
        p_a, idx_a = pos[a]
        p_b, _ = pos[b]

        moving_blocks = stacks[p_a][idx_a:]
        stacks[p_a] = stacks[p_a][:idx_a]

        for block in moving_blocks:
            pos[block] = (p_b, len(stacks[p_b]))
            stacks[p_b].append(block)

    # Print the final state
    for i in range(n):
        if stacks[i]:
            print(f"{i}: " + " ".join(map(str, stacks[i])))
        else:
            print(f"{i}:")

if __name__ == '__main__':
    solve()