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
    import sys

    for line in sys.stdin:
        line = line.strip()

        if not line:
            continue

        i, j = map(int, line.split())

        lower = min(i, j)
        upper = max(i, j)

        max_length = 0

        for n in range(lower, upper + 1):
            length = cycle_length(n)

            if length > max_length:
                max_length = length

        print(i, j, max_length)


if __name__ == "__main__":
    main()