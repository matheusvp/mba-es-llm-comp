import sys

def main():
    data = sys.stdin.read()
    result = []
    open_quote = True
    for ch in data:
        if ch == '"':
            result.append("``" if open_quote else "''")
            open_quote = not open_quote
        else:
            result.append(ch)
    sys.stdout.write(''.join(result))

if __name__ == "__main__":
    main()