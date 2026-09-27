import sys

def main():
    data = sys.stdin.read().split('\n')
    idx = 0
    n = int(data[idx].strip())
    idx += 1

    positions = [[i] for i in range(n)]

    def find_block(b):
        for p in range(n):
            for h in range(len(positions[p])):
                if positions[p][h] == b:
                    return p, h
        return -1, -1

    def move_back(pile_idx, height):
        # move everything above 'height' back to their initial positions
        pile = positions[pile_idx]
        movers = pile[height + 1:]
        del pile[height + 1:]
        for block in movers:
            positions[block].append(block)

    while idx < len(data):
        line = data[idx].strip()
        idx += 1
        if not line:
            continue
        if line == "quit":
            break

        tokens = line.split()
        if len(tokens) < 4:
            continue

        cmd = tokens[0]
        a = int(tokens[1])
        keyword = tokens[2]
        b = int(tokens[3])

        if a == b:
            continue

        pa, ha = find_block(a)
        pb, hb = find_block(b)

        if pa == pb:
            continue

        if cmd == "move":
            move_back(pa, ha)
            pa, ha = find_block(a)
            if keyword == "onto":
                move_back(pb, hb)
            block_to_move = positions[pa][ha]
            del positions[pa][ha:]
            positions[pb].append(block_to_move)
        elif cmd == "pile":
            movers = positions[pa][ha:]
            del positions[pa][ha:]
            if keyword == "onto":
                move_back(pb, hb)
            positions[pb].extend(movers)

    output_lines = []
    for p in range(n):
        if positions[p]:
            output_lines.append(f"{p}: " + " ".join(map(str, positions[p])))
        else:
            output_lines.append(f"{p}:")

    sys.stdout.write("\n".join(output_lines) + "\n")

if __name__ == "__main__":
    main()