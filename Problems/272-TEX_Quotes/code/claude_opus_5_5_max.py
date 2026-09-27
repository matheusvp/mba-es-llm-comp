import sys


def main():
    reader = sys.stdin.buffer
    writer = sys.stdout.buffer
    opening = True  # whether the next '"' opens a quotation; persists across lines

    for line in reader:
        pieces = line.split(b'"')
        out = [pieces[0]]
        for piece in pieces[1:]:
            out.append(b"``" if opening else b"''")
            opening = not opening
            out.append(piece)
        writer.write(b"".join(out))

    writer.flush()


if __name__ == "__main__":
    main()