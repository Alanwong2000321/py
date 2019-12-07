ppppp = 0
while True:
    oo = []
    p = []
    n = input()
    if n == "EOF":
        break
    a = int(input())
    for o in n:
        p.append(o)
    t1 = int(p[0])*10*60
    t2 = int(p[1])*60
    t3 = int(p[3])*10
    t4 = int(p[-1])
    time = t1 + t2 + t3 + t4 + a
    if time >= 1440:
        while True:
            if time <= 1440:
                break
            time -= 1440
    s = int(time//60)
    if s % 24 == 0:
        cc = '00'
    else:
        cc = s
    f = int(time - s * 60)
    if f >= 10:
        tt = f
    elif f == 9:
        tt = '09'
    elif f == 8:
        tt = '08'
    elif f == 7:
        tt = '07'
    elif f == 6:
        tt = '06'
    elif f == 5:
        tt = '05'
    elif f == 4:
        tt = '04'
    elif f == 3:
        tt = '03'
    elif f == 2:
        tt = '02'
    elif f == 1:
        tt = '01'
    elif f == 0:
        tt = '00'
    oo.append(cc)
    oo.append(":")
    oo.append(tt)
    for pop in oo:
        ppppp += 1
        print(pop,end="")
        if ppppp % 3 == 0:
            print()