import sys

def main():
    data = sys.stdin.buffer.read()
    out = bytearray()
    open_quote = True
    for b in data:
        if b == 34:
            if open_quote:
                out += b"``"
            else:
                out += b"''"
            open_quote = not open_quote
        else:
            out.append(b)
    sys.stdout.buffer.write(bytes(out))
    sys.stdout.buffer.flush()

if __name__ == "__main__":
    main()