import sys

memo = {1: 1}

def get_cycle_length(n):
    curr = n
    path = []
    while curr not in memo:
        path.append(curr)
        if curr % 2 == 0:
            curr //= 2
        else:
            curr = 3 * curr + 1
    
    base_len = memo[curr]
    for step, val in enumerate(reversed(path), start=1):
        memo[val] = base_len + step
        
    return memo[n]

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    for idx in range(0, len(input_data), 2):
        if idx + 1 >= len(input_data):
            break
        i = int(input_data[idx])
        j = int(input_data[idx + 1])
        
        low = min(i, j)
        high = max(i, j)
        
        max_cycle = 0
        for num in range(low, high + 1):
            length = get_cycle_length(num)
            if length > max_cycle:
                max_cycle = length
                
        print(f"{i} {j} {max_cycle}")

if __name__ == '__main__':
    main()