a, b, c, d= [int(x) for x in input().split()]
n = a * 5 +  b *12 + c*15 
k = d * 0.7
if n >= 100:
    if k >= 60:
        print('Pass')
    else:
        print('Fail')
else:
    v = (100 - n ) * 0.3 + k
    if v >= 60:
        print('Pass')
    else:
        print('Fail')