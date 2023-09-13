# Stairs

def countStairs(lower, n):
    if n == 0:
        return 1
    count = 0
    for i in range(lower):
        if n - i < 0:
            break
        count += countStairs(i, n-i)
    return count

N = 7
print(countStairs(N+1,N))