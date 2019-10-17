k = int(input())
s = 0
i = 1 
while s + 1 / i<= k:
    s += 1 / i
    i += 1
print(i)