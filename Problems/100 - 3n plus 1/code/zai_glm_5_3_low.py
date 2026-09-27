import sys

def cycle_length(n, memo):
    path = []
    orig = n
    while n != 1 and n not in memo:
        path.append(n)
        if n % 2:
            n = 3 * n + 1
        else:
            n //= 2
    length = memo.get(n, 1)
    for i, v in enumerate(reversed(path)):
        memo[v] = length + i + 1
    return memo[orig]

def main():
    data = sys.stdin.read().split()
    memo = {1: 1}
    out = []
    for k in range(0, len(data) - 1, 2):
        i, j = int(data[k]), int(data[k + 1])
        lo, hi = min(i, j), max(i, j)
        best = 0
        for n in range(lo, hi + 1):
            c = cycle_length(n, memo)
            if c > best:
                best = c
        out.append(f"{i} {j} {best}")
    print("\n".join(out))

main()