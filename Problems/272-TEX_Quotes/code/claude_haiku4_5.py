import sys

open_quote = False

for char in sys.stdin.read():
    if char == '"':
        if open_quote:
            print("''", end='')
        else:
            print("``", end='')
        open_quote = not open_quote
    else:
        print(char, end='')