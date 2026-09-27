import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
        
    n = int(input_data[0])
    stacks = [[i] for i in range(n)]
    
    def find_block(x):
        for p in range(n):
            for h in range(len(stacks[p])):
                if stacks[p][h] == x:
                    return p, h
        return -1, -1

    def return_above(p, h):
        for block in stacks[p][h+1:]:
            stacks[block].append(block)
        del stacks[p][h+1:]

    idx = 1
    while idx < len(input_data):
        if input_data[idx] == 'quit':
            break
        
        cmd1 = input_data[idx]
        a = int(input_data[idx+1])
        cmd2 = input_data[idx+2]
        b = int(input_data[idx+3])
        idx += 4
        
        if a == b:
            continue
            
        pa, ha = find_block(a)
        pb, hb = find_block(b)
        
        if pa == pb:
            continue
            
        if cmd1 == 'move':
            return_above(pa, ha)
        if cmd2 == 'onto':
            return_above(pb, hb)
            
        stacks[pb].extend(stacks[pa][ha:])
        del stacks[pa][ha:]

    for i in range(n):
        if stacks[i]:
            print(f"{i}: " + " ".join(map(str, stacks[i])))
        else:
            print(f"{i}:")

if __name__ == '__main__':
    main()