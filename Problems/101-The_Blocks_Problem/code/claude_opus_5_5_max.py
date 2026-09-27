aimport sys


def main():
    readline = sys.stdin.readline

    # The first non-empty line holds n.
    while True:
        line = readline()
        if not line:
            return
        tokens = line.split()
        if tokens:
            break
    try:
        n = int(tokens[0])
    except ValueError:
        return

    stacks = [[i] for i in range(n)]  # stacks[p]: blocks at position p, bottom to top
    where = list(range(n))            # where[b]: position of the stack holding block b

    def clear_above(block):
        # Return every block stacked on top of `block` to its initial position.
        stack = stacks[where[block]]
        idx = stack.index(block)
        for other in stack[idx + 1:]:
            stacks[other].append(other)
            where[other] = other
        del stack[idx + 1:]

    def transfer(a, b):
        # Move `a` together with everything above it onto the top of b's stack.
        src = stacks[where[a]]
        idx = src.index(a)
        chunk = src[idx:]
        del src[idx:]
        dest = where[b]
        stacks[dest].extend(chunk)
        for block in chunk:
            where[block] = dest

    while True:
        line = readline()
        if not line:
            break  # EOF
        tokens = line.split()
        if not tokens:
            continue
        if tokens[0] == "quit":
            break
        if len(tokens) != 4:
            continue
        verb, a, prep, b = tokens
        if verb not in ("move", "pile") or prep not in ("onto", "over"):
            continue
        try:
            a = int(a)
            b = int(b)
        except ValueError:
            continue
        if not (0 <= a < n and 0 <= b < n):
            continue
        if a == b or where[a] == where[b]:
            continue  # illegal command: ignore

        if verb == "move":
            clear_above(a)
        if prep == "onto":
            clear_above(b)
        transfer(a, b)

    out = []
    for i in range(n):
        if stacks[i]:
            out.append("%d: %s" % (i, " ".join(map(str, stacks[i]))))
        else:
            out.append("%d:" % i)
    sys.stdout.write("".join(row + "\n" for row in out))


if __name__ == "__main__":
    main()