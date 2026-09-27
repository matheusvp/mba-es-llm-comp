import sys


def main():
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    stacks = [[i] for i in range(n)]
    pos = list(range(n))

    def return_above(x):
        s = stacks[pos[x]]
        idx = s.index(x)
        for blk in s[idx + 1:]:
            stacks[blk].append(blk)
            pos[blk] = blk
        del s[idx + 1:]

    i = 1
    while i < len(data):
        cmd = data[i]
        if cmd == "quit":
            break
        if i + 3 >= len(data):
            break
        try:
            a = int(data[i + 1])
            b = int(data[i + 3])
        except ValueError:
            i += 1
            continue
        mode = data[i + 2]
        i += 4
        if cmd not in ("move", "pile") or mode not in ("onto", "over"):
            continue
        if not (0 <= a < n and 0 <= b < n) or a == b or pos[a] == pos[b]:
            continue
        if cmd == "move":
            return_above(a)
        if mode == "onto":
            return_above(b)
        src = stacks[pos[a]]
        idx = src.index(a)
        moving = src[idx:]
        del src[idx:]
        dest = pos[b]
        stacks[dest].extend(moving)
        for blk in moving:
            pos[blk] = dest

    out = []
    for k in range(n):
        if stacks[k]:
            out.append(f"{k}: " + " ".join(map(str, stacks[k])))
        else:
            out.append(f"{k}:")
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()