import sys


def main():
    tokens = sys.stdin.buffer.read().split()
    pair_count = len(tokens) // 2
    if pair_count == 0:
        return

    nums = list(map(int, tokens[:2 * pair_count]))
    top = max(1, max(nums))

    # cycle[n] holds the cycle length of n. Values are filled in increasing
    # order, so every number smaller than n is already known when n is reached.
    cycle = [0] * (top + 1)
    cycle[1] = 1
    for n in range(2, top + 1):
        if not n & 1:
            # Even: n -> n/2.
            cycle[n] = cycle[n >> 1] + 1
        elif not n & 2:
            # n = 1 (mod 4): n -> 3n+1 -> (3n+1)/2 -> (3n+1)/4, which is below n.
            cycle[n] = cycle[(3 * n + 1) >> 2] + 3
        else:
            # n = 3 (mod 4): follow the sequence until it drops below n.
            x = n
            steps = 0
            while x >= n:
                if x & 1:
                    x = (3 * x + 1) >> 1  # 3x+1 is always even, so halve it at once
                    steps += 2
                else:
                    x >>= 1
                    steps += 1
            cycle[n] = cycle[x] + steps

    # Maximum cycle length of each block of 1024 consecutive numbers, so a
    # range query only scans two partial blocks plus a short list of maxima.
    shift = 10
    block_max = [max(cycle[b << shift:(b + 1) << shift])
                 for b in range((top >> shift) + 1)]

    out = []
    for k in range(0, 2 * pair_count, 2):
        i = nums[k]
        j = nums[k + 1]
        lo, hi = (i, j) if i <= j else (j, i)
        if lo < 1:  # inputs are guaranteed positive; guard against bad data anyway
            lo = 1
        if hi < lo:
            best = 0
        else:
            first = lo >> shift
            last = hi >> shift
            if last - first < 2:
                best = max(cycle[lo:hi + 1])
            else:
                best = max(max(cycle[lo:(first + 1) << shift]),
                           max(block_max[first + 1:last]),
                           max(cycle[last << shift:hi + 1]))
        out.append("%d %d %d" % (i, j, best))

    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()