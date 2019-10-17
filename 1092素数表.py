import math 
def is_prime(n):
    if n < 2:
        return False
    for j in range(2, int(math.sqrt(n)) + 1):
        if n % j == 0:
            return False
    return True
m, n = [int(x) for x in input().split()]
for i in range(m, n+1):
    if is_prime(i):
        print("%d " % i, end="")