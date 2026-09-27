import sys
from array import array


def main():
    data = sys.stdin.buffer.read().split()
    if not data:
        return

    LIMIT = 1 << 21
    cache = array("H", [0]) * LIMIT
    cache[1] = 1

    out = []
    pos = 0
    count = len(data)
    while pos + 1 < count:
        i = int(data[pos])
        j = int(data[pos + 1])
        pos += 2
        lo, hi = (i, j) if i <= j else (j, i)

        best = 0
        for n in range(lo, hi + 1):
            c = cache[n]
            if c:
                if c > best:
                    best = c
                continue

            path = [n]
            m = n
            while True:
                if m & 1:
                    m = 3 * m + 1
                else:
                    m >>= 1
                if m < LIMIT:
                    c = cache[m]
                    if c:
                        break
                path.append(m)

            for v in reversed(path):
                c += 1
                if v < LIMIT:
                    cache[v] = c

            if c > best:
                best = c

        out.append("%d %d %d" % (i, j, best))

    if out:
        sys.stdout.write("\n".join(out) + "\n")


main()