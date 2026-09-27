import sys

def solve():
    cache = {1: 1}
    
    for line in sys.stdin:
        tokens = line.split()
        if not tokens:
            continue
        
        for idx in range(0, len(tokens), 2):
            if idx + 1 >= len(tokens):
                break
                
            i = int(tokens[idx])
            j = int(tokens[idx+1])
            
            start = i if i < j else j
            end = j if i < j else i
            
            max_cycle = 0
            for n in range(start, end + 1):
                curr = n
                count = 0
                
                while curr not in cache:
                    if curr % 2 == 1:
                        curr = 3 * curr + 1
                    else:
                        curr = curr // 2
                    count += 1
                
                cycle_len = cache[curr] + count
                cache[n] = cycle_len
                
                if cycle_len > max_cycle:
                    max_cycle = cycle_len
                    
            print(f"{i} {j} {max_cycle}")

if __name__ == '__main__':
    solve()