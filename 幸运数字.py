find = False
m, n = [int(x) for x in input().split()]
for i in range(n, m-1, -1):
    if i % 7 == 0 and i % 4 != 0:
        print(i)
        find = True
        break
if not find:
    print("no")
