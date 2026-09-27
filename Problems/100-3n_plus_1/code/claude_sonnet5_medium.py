import sys

def cycle_length(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        length += 1
    return length

def main():
    cache = {}
    out_lines = []
    for line in sys.stdin:
        parts = line.split()
        if len(parts) < 2:
            continue
        i, j = int(parts[0]), int(parts[1])
        lo, hi = min(i, j), max(i, j)
        max_len = 0
        for n in range(lo, hi + 1):
            if n in cache:
                l = cache[n]
            else:
                l = cycle_length(n)
                cache[n] = l
            if l > max_len:
                max_len = l
        out_lines.append(f"{i} {j} {max_len}")
    sys.stdout.write("\n".join(out_lines) + ("\n" if out_lines else ""))

if __name__ == "__main__":
    main()