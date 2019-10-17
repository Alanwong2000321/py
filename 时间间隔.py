def a(s):
    h,m,s=int(s[:2]),int(s[3:5]),int(s[6:8])
    return 3600*h+m*60+s
while True:
    s1=input()
    if not s1:
        break
    s2=input()
    t=a(s2)-a(s1)
    h=(t//3600)%24
    m=t%3600//60
    s=t%60
    print("%02d:%02d:%02d" % (h,m,s))