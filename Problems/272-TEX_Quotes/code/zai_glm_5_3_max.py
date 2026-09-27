import sys


def main():
    # Read the entire input as raw bytes until EOF.
    # This guarantees every character (spaces, tabs, newlines, \r\n, etc.)
    # is preserved exactly as it appeared in the input.
    data = sys.stdin.buffer.read()

    # Splitting on the double-quote byte yields n+1 chunks for n quotes.
    # Chunk indices 1..n correspond to the positions of the quotes:
    # odd indices are opening quotes, even indices are closing quotes.
    # Since the quote count is guaranteed even, this alternation is exact,
    # and the open/close state naturally persists across line boundaries
    # because the whole input is treated as one continuous stream.
    parts = data.split(b'"')

    out = bytearray(parts[0])
    for i in range(1, len(parts)):
        if i % 2 == 1:
            out += b'``'      # opening double quote -> two backticks
        else:
            out += b"''"      # closing double quote -> two apostrophes
        out += parts[i]

    sys.stdout.buffer.write(bytes(out))


if __name__ == '__main__':
    main()
