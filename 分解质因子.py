n = int(input())
i = 2
while n > 1:
    if n % i == 0:
        n = n / i 
        print(i,end=' ')
    else:
        i += 1
        if n == 1:
            print('\n')