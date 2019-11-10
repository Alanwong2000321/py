while True:
    def shuixianhua(num):
        a = num % 10
        b = (num // 10) % 10
        c = num // 100
        if a**3 + b**3 + c**3 == num:
            return num
        else:
            return False
    n, m = [int(z) for z in input().split()]
    nums = [int(z) for z in range(n,m+1) if shuixianhua(z)]
    if not nums:
        print('no')
    else:
        print(*nums)