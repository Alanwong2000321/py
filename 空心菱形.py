def xinxin(h):
    i = 1
    while i <= h:
        i += 1
        print(' ',end='')
    print('*',end='')
n = int(input())
i = -(n - 1)
while i <= n - 1:
    if i == -(n - 1) or i == n - 1:
        xinxin(abs(i))
    else:
        xinxin(abs(i))
        xinxin((n - abs(i) - 1)* 2 -1 )
    i += 1
    print('')