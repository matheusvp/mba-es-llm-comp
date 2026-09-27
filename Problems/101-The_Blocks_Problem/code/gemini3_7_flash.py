import sys


def solve():
    tokens = sys.stdin.read().split()
    if not tokens:
        return

    n = int(tokens[0])
    stacks = [[i] for i in range(n)]

    def find_block(block):
        for stack_idx, stack in enumerate(stacks):
            if block in stack:
                return stack_idx, stack.index(block)
        return -1, -1

    def clear_above(block):
        stack_idx, block_idx = find_block(block)
        above_blocks = stacks[stack_idx][block_idx + 1 :]
        stacks[stack_idx] = stacks[stack_idx][: block_idx + 1]
        for b in above_blocks:
            stacks[b].append(b)

    cursor = 1
    while cursor < len(tokens):
        cmd1 = tokens[cursor]
        if cmd1 == "quit":
            break

        a = int(tokens[cursor + 1])
        cmd2 = tokens[cursor + 2]
        b = int(tokens[cursor + 3])
        cursor += 4

        if a == b:
            continue

        pos_a, _ = find_block(a)
        pos_b, _ = find_block(b)
        if pos_a == pos_b:
            continue

        if cmd1 == "move":
            clear_above(a)
            if cmd2 == "onto":
                clear_above(b)
            pos_a, idx_a = find_block(a)
            pos_b, _ = find_block(b)
            stacks[pos_b].append(stacks[pos_a].pop())

        elif cmd1 == "pile":
            if cmd2 == "onto":
                clear_above(b)
            pos_a, idx_a = find_block(a)
            pos_b, _ = find_block(b)
            pile_to_move = stacks[pos_a][idx_a:]
            stacks[pos_a] = stacks[pos_a][:idx_a]
            stacks[pos_b].extend(pile_to_move)

    for i in range(n):
        if stacks[i]:
            print(f"{i}: {' '.join(map(str, stacks[i]))}")
        else:
            print(f"{i}:")


if __name__ == "__main__":
    solve()