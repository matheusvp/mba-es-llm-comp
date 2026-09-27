import sys


def main():
    data = sys.stdin.read().split()
    if not data:
        return

    pos = 0
    n = int(data[pos])
    pos += 1

    piles = [[i] for i in range(n)]

    def locate(block):
        for i, pile in enumerate(piles):
            for j, val in enumerate(pile):
                if val == block:
                    return i, j
        return -1, -1

    def return_above(pile_idx, height):
        pile = piles[pile_idx]
        while len(pile) > height + 1:
            block = pile.pop()
            piles[block].append(block)

    while pos < len(data):
        cmd = data[pos]
        if cmd == 'quit':
            break
        if pos + 3 >= len(data):
            break

        a = int(data[pos + 1])
        prep = data[pos + 2]
        b = int(data[pos + 3])
        pos += 4

        if cmd not in ('move', 'pile') or prep not in ('onto', 'over'):
            continue
        if a == b or not (0 <= a < n) or not (0 <= b < n):
            continue

        pa, ha = locate(a)
        pb, hb = locate(b)
        if pa == -1 or pb == -1 or pa == pb:
            continue

        if cmd == 'move':
            return_above(pa, ha)
        if prep == 'onto':
            return_above(pb, hb)

        pa, ha = locate(a)
        pb, hb = locate(b)

        moving = piles[pa][ha:]
        del piles[pa][ha:]
        piles[pb].extend(moving)

    out = []
    for i in range(n):
        if piles[i]:
            out.append('%d: %s' % (i, ' '.join(str(x) for x in piles[i])))
        else:
            out.append('%d:' % i)
    sys.stdout.write('\n'.join(out) + '\n')


if __name__ == '__main__':
    main()