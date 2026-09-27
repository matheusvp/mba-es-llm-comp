import sys


def solve():
    input_iter = iter(sys.stdin)
    first_line = ""
    for line in input_iter:
        line = line.strip()
        if line:
            first_line = line
            break
    if not first_line:
        return

    n = int(first_line)
    piles = [[i] for i in range(n)]

    def find_block(val):
        for p in range(n):
            for h in range(len(piles[p])):
                if piles[p][h] == val:
                    return p, h
        return -1, -1

    def clear_above(p, h):
        to_clear = piles[p][h + 1:]
        del piles[p][h + 1:]
        for blk in to_clear:
            piles[blk].append(blk)

    for line in input_iter:
        line = line.strip()
        if not line:
            continue
        if line == "quit":
            break

        parts = line.split()
        if len(parts) != 4:
            continue

        cmd1, a_str, cmd2, b_str = parts
        try:
            a = int(a_str)
            b = int(b_str)
        except ValueError:
            continue

        if a == b or a < 0 or a >= n or b < 0 or b >= n:
            continue

        pa, ha = find_block(a)
        pb, hb = find_block(b)

        if pa == pb:
            continue

        if cmd1 == "move":
            clear_above(pa, ha)
            moving = [piles[pa].pop()]
        elif cmd1 == "pile":
            moving = piles[pa][ha:]
            del piles[pa][ha:]
        else:
            continue

        if cmd2 == "onto":
            clear_above(pb, hb)
        elif cmd2 != "over":
            continue

        piles[pb].extend(moving)

    for i in range(n):
        if piles[i]:
            print(f"{i}: {' '.join(map(str, piles[i]))}")
        else:
            print(f"{i}:")


if __name__ == "__main__":
    solve()