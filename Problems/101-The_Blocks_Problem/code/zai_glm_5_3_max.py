import sys


def main():
    data = sys.stdin.read().split('\n')
    idx = 0

    # Read n, skipping any blank lines
    while idx < len(data) and data[idx].strip() == '':
        idx += 1
    n = int(data[idx].strip())
    idx += 1

    # blocks[p] = list of blocks at position p, ordered bottom to top
    blocks = [[i] for i in range(n)]
    # pos[b] = current position of block b
    pos = list(range(n))

    def return_above(p, b):
        # Return all blocks above block b (at position p) to their home positions
        i = blocks[p].index(b)
        above = blocks[p][i + 1:]
        del blocks[p][i + 1:]
        for x in above:
            blocks[x].append(x)
            pos[x] = x

    line_idx = idx
    while line_idx < len(data):
        line = data[line_idx].strip()
        line_idx += 1
        if not line:
            continue
        parts = line.split()
        if parts[0] == 'quit':
            break
        if len(parts) != 4:
            continue
        verb1, a_str, verb2, b_str = parts
        try:
            a = int(a_str)
            b = int(b_str)
        except ValueError:
            continue
        if not (0 <= a < n and 0 <= b < n):
            continue
        # Illegal command: a == b or blocks in the same stack
        if a == b or pos[a] == pos[b]:
            continue

        pa, pb = pos[a], pos[b]

        if verb1 == 'move':
            return_above(pa, a)
            if verb2 == 'onto':
                return_above(pb, b)
            blocks[pa].remove(a)
            blocks[pb].append(a)
            pos[a] = pb
        elif verb1 == 'pile':
            i = blocks[pa].index(a)
            pile = blocks[pa][i:]
            del blocks[pa][i:]
            if verb2 == 'onto':
                return_above(pb, b)
            for x in pile:
                blocks[pb].append(x)
                pos[x] = pb

    out = []
    for i in range(n):
        if blocks[i]:
            out.append(str(i) + ': ' + ' '.join(str(x) for x in blocks[i]))
        else:
            out.append(str(i) + ':')
    sys.stdout.write('\n'.join(out) + '\n')


main()