import sys

def main():
    data = sys.stdin.read().split('\n')
    n = int(data[0])
    stacks = [[i] for i in range(n)]
    pos = [i for i in range(n)]

    def find(a):
        return pos[a]

    def return_above(s, block):
        stack = stacks[s]
        idx = stack.index(block)
        while len(stack) > idx + 1:
            b = stack.pop()
            stacks[b].append(b)
            pos[b] = b

    for line in data[1:]:
        parts = line.split()
        if len(parts) < 4:
            continue
        cmd, a, mode, b = parts[0], int(parts[1]), parts[2], int(parts[3])
        if cmd == 'quit':
            break
        if cmd not in ('move', 'pile'):
            continue
        if a == b or pos[a] == pos[b]:
            continue
        sa, sb = pos[a], pos[b]
        if cmd == 'move':
            return_above(sa, a)
            if mode == 'onto':
                return_above(sb, b)
            stacks[sb].append(stacks[sa].pop())
            pos[a] = sb
        else:  # pile
            if mode == 'onto':
                return_above(sb, b)
            stack_a = stacks[sa]
            idx = stack_a.index(a)
            moved = stack_a[idx:]
            del stack_a[idx:]
            for blk in moved:
                stacks[sb].append(blk)
                pos[blk] = sb

    out = []
    for i in range(n):
        if stacks[i]:
            out.append(f"{i}: " + ' '.join(map(str, stacks[i])))
        else:
            out.append(f"{i}:")
    print('\n'.join(out))

main()