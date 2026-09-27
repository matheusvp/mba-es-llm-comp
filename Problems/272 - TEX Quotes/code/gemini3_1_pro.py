import sys

def main():
    input_text = sys.stdin.read()
    output = []
    is_open = True
    
    for char in input_text:
        if char == '"':
            if is_open:
                output.append("``")
            else:
                output.append("''")
            is_open = not is_open
        else:
            output.append(char)
            
    sys.stdout.write("".join(output))

if __name__ == '__main__':
    main()