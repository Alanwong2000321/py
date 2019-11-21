mport random
count=0
a=[[0 for i in range(6)]for i in range(6)]
print("随机生成一个6*6的二维数组做为棋盘中的权值：")
for i in range(6):
    for j in range(6):
        a[i][j] = random.randint(100, 1000)
        print('%2d'%a[i][j],end=" ")
        count+=1
        if count%6==0:
            print("\n")
for i in range(1,6):
    a[0][i]=a[0][i-1]+a[0][i]
    a[i][0]=a[i-1][0]+a[i][0]
for i in range(1,6):
    for j in range(1,6):
        a[i][j]=max(a[i-1][j],a[i][j-1])+a[i][j]
print("变化后的数组：")
for i in range(6):
    for j in range(6):
        print('%2d'%a[i][j],end=" ")
        count+=1
        if count%6==0:
            print("\n")
print("最终得最大值为%d" %a[5][5])