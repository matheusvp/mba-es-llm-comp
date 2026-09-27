import sys


def main():
    text = sys.stdin.read()
    if not text:
        return

    result = []
    open_quote = True

    for char in text:
        if char == '"':
            if open_quote:
                result.append("``")
            else:
                result.append("''")
            open_quote = not open_quote
        else:
            result.append(char)

    sys.stdout.write("".join(result))


if __name__ == "__main__":
    main()