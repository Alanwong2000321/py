a = input()
p = a[-1]
c = 0
for i in a[:-1]:
    if i == p:
        c += 1
print(c)