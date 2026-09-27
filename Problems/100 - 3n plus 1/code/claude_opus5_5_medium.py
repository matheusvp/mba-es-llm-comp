import sys


def main():
    data = sys.stdin.read().split()
    pairs = []
    for k in range(0, len(data) - 1, 2):
        pairs.append((int(data[k]), int(data[k + 1])))

    if not pairs:
        return

    limit = max(max(a, b) for a, b in pairs)

    cache = [0] * (limit + 1)
    cache[1] = 1
    for n in range(2, limit + 1):
        if n & 1 == 0:
            cache[n] = cache[n >> 1] + 1
            continue
        x = n
        steps = 0
        while x >= n:
            if x & 1:
                x = (3 * x + 1) >> 1
                steps += 2
            else:
                x >>= 1
                steps += 1
        cache[n] = steps + cache[x]

    out = []
    for i, j in pairs:
        lo, hi = (i, j) if i <= j else (j, i)
        best = max(cache[lo:hi + 1])
        out.append("%d %d %d" % (i, j, best))

    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()