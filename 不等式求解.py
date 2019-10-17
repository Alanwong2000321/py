def fac(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s
 
m = 1
sums = 0
n = int(input())
result = 0
while sums + fac(m) < n:
    sums += fac(m)
    result = m
    m += 1
print("m<=%d" % result)