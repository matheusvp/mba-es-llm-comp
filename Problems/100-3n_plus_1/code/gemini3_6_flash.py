import sys


def get_cycle_length(n, memo={1: 1}):
    if n in memo:
        return memo[n]

    if n % 2 == 0:
        length = 1 + get_cycle_length(n // 2, memo)
    else:
        # Pre-calculated optimization: 3n + 1 is guaranteed to be even,
        # so we do (3n + 1) // 2 and add 2 steps directly.
        length = 2 + get_cycle_length((3 * n + 1) // 2, memo)

    memo[n] = length
    return length


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    memo = {1: 1}

    for idx in range(0, len(input_data), 2):
        if idx + 1 >= len(input_data):
            break

        i_orig = int(input_data[idx])
        j_orig = int(input_data[idx + 1])

        low = min(i_orig, j_orig)
        high = max(i_orig, j_orig)

        max_len = 0
        for n in range(low, high + 1):
            length = get_cycle_length(n, memo)
            if length > max_len:
                max_len = length

        print(f"{i_orig} {j_orig} {max_len}")


if __name__ == "__main__":
    main()