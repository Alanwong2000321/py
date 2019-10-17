n = int(input())
t = int(input())
kobe = False
for man in range(n):
    for women in range(n):
        for child in range(n):
            if man * 3 + women * 2 + child == t:
                    if man + women + child * 3 == n:
                        kobe = True
                        print("%4d%4d%4d"%(man,women,child * 3))
if not kobe:                    
    print("No Answer")
