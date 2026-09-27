import sys

def main():
    data = sys.stdin.read()
    out = []
    open_quote = True
    for ch in data:
        if ch == '"':
            out.append('``' if open_quote else "''")
            open_quote = not open_quote
        else:
            out.append(ch)
    sys.stdout.write(''.join(out))

if __name__ == '__main__':
    main()