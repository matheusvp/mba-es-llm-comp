import sys

cache = {1: 1}

def cycle_length(n):
    """Calculate the cycle length for a given number n."""
    if n in cache:
        return cache[n]
    
    original_n = n
    path = []
    
    # Follow the sequence until we hit a cached value
    while n not in cache:
        path.append(n)
        if n % 2 == 1:  # n is odd
            n = 3 * n + 1
        else:  # n is even
            n = n // 2
    
    # Backtrack and cache all values in the path
    length = cache[n]
    for i in range(len(path) - 1, -1, -1):
        length += 1
        cache[path[i]] = length
    
    return cache[original_n]

def max_cycle_length(i, j):
    """Find the maximum cycle length for all integers between i and j (inclusive)."""
    if i > j:
        i, j = j, i
    
    max_length = 0
    for n in range(i, j + 1):
        length = cycle_length(n)
        max_length = max(max_length, length)
    
    return max_length

# Read input until EOF
for line in sys.stdin:
    parts = line.split()
    if len(parts) < 2:
        continue
    
    i = int(parts[0])
    j = int(parts[1])
    
    max_len = max_cycle_length(i, j)
    
    # Output in the original order of i and j
    print(i, j, max_len)