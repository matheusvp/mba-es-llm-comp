import sys


def main():
    cache = {1: 1}

    def cycle_length(n):
        stack = []
        while n not in cache:
            stack.append(n)
            n = 3 * n + 1 if n & 1 else n >> 1
        length = cache[n]
        while stack:
            length += 1
            cache[stack.pop()] = length
        return length

    out = []
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 2:
            continue
        i, j = int(parts[0]), int(parts[1])
        lo, hi = (i, j) if i <= j else (j, i)
        best = 0
        for n in range(lo, hi + 1):
            c = cycle_length(n)
            if c > best:
                best = c
        out.append("%d %d %d" % (i, j, best))

    sys.stdout.write("\n".join(out) + ("\n" if out else ""))


if __name__ == "__main__":
    main()