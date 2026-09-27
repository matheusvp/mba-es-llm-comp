import sys

def main():
    is_open = True

    for line in sys.stdin:
        result = []

        for char in line:
            if char == '"':
                if is_open:
                    result.append("``")
                else:
                    result.append("''")

                is_open = not is_open
            else:
                result.append(char)

        sys.stdout.write("".join(result))


if __name__ == "__main__":
    main()