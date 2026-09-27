import sys


def main():
    open_quote = True
    for line in sys.stdin:
        res = []
        for ch in line:
            if ch == '"':
                if open_quote:
                    res.append("``")
                else:
                    res.append("''")
                open_quote = not open_quote
            else:
                res.append(ch)
        sys.stdout.write("".join(res))


if __name__ == "__main__":
    main()