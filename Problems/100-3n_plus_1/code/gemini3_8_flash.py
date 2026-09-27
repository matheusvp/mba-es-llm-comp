import sys


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    memo = {1: 1}

    def get_cycle_length(n):
        path = []
        curr = n
        while curr not in memo:
            path.append(curr)
            if curr % 2:
                curr = 3 * curr + 1
            else:
                curr //= 2

        base_length = memo[curr]
        for step, val in enumerate(reversed(path), 1):
            memo[val] = base_length + step

        return memo[n]

    results = []
    for idx in range(0, len(input_data), 2):
        if idx + 1 >= len(input_data):
            break

        orig_i = int(input_data[idx])
        orig_j = int(input_data[idx + 1])

        low, high = (orig_i, orig_j) if orig_i <= orig_j else (orig_j, orig_i)

        max_cycle = 0
        for num in range(low, high + 1):
            length = get_cycle_length(num)
            if length > max_cycle:
                max_cycle = length

        results.append(f"{orig_i} {orig_j} {max_cycle}")

    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    main()