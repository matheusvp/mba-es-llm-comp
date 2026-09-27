import sys

def solve():
    open_quote = True
    input_text = sys.stdin.read()
    output = []
    
    for char in input_text:
        if char == '"':
            if open_quote:
                output.append("``")
            else:
                output.append("''")
            open_quote = not open_quote
        else:
            output.append(char)
            
    sys.stdout.write("".join(output))

if __name__ == "__main__":
    solve()