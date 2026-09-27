import sys

def main():
    data = sys.stdin.read()
    out = []
    open_quote = True
    for ch in data:
        if ch == '"':
            if open_quote:
                out.append("``")
            else:
                out.append("''")
            open_quote = not open_quote
        else:
            out.append(ch)
    sys.stdout.write(''.join(out))

main()