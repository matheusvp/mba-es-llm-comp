def find_block(stacks, block):
    for i, stack in enumerate(stacks):
        if block in stack:
            return i, stack.index(block)
    return -1, -1


def clear_above(stacks, stack_index, position):
    """Return all blocks above the given position to their home positions."""
    stack = stacks[stack_index]

    while len(stack) > position + 1:
        block = stack.pop()
        stacks[block].append(block)


n = int(input().strip())

# stacks[i] is initially the stack at position i
stacks = [[i] for i in range(n)]

while True:
    command_line = input().strip()

    if command_line == "quit":
        break

    command, mode, a_str, b_str = command_line.split()
    a = int(a_str)
    b = int(b_str)

    stack_a, pos_a = find_block(stacks, a)
    stack_b, pos_b = find_block(stacks, b)

    # Ignore illegal commands
    if a == b or stack_a == stack_b:
        continue

    if command == "move":
        # Return blocks above a.
        clear_above(stacks, stack_a, pos_a)

        # Re-find b's stack because stack indices may still be valid,
        # but this keeps the logic straightforward.
        stack_b, pos_b = find_block(stacks, b)

        # Remove a from its current stack.
        stacks[stack_a].pop()

        if mode == "onto":
            # Return blocks above b.
            clear_above(stacks, stack_b, pos_b)

        # Put a on top of b's stack.
        stacks[stack_b].append(a)

    else:  # command == "pile"
        # Save a and everything above it.
        pile = stacks[stack_a][pos_a:]
        del stacks[stack_a][pos_a:]

        if mode == "onto":
            # Return blocks above b.
            clear_above(stacks, stack_b, pos_b)

        # Put the pile on top of b's stack.
        stacks[stack_b].extend(pile)

# Output
for i in range(n):
    if stacks[i]:
        print(f"{i}: " + " ".join(map(str, stacks[i])))
    else:
        print(f"{i}:")