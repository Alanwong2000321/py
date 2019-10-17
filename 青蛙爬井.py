high, up, day = [int(x) for x in input().split()]
c = 0
days = 0
while c < high:
    c += up
    days += 1
    if cur >= high:
        break
    c -= day
print(days)