di = 0
x = 0
y = 0
time1 = 0
while True:
    time = int(input())
    command = int(input()) 
    if di == 1:
        x += 10*(time-time1)
    elif di == 2:
        y -= 10*(time-time1)
    elif di == 3:
        x -= 10*(time-time1)
    else:
        y += 10*(time-time1)
    time1 = time 
    if command == 3:
        break
    elif command == 1:
        if di == 0:
            di = 3
        else:
            di = di - 1
    else:
        if di == 3:
            di = 0
        else:
            di = di + 1
print(x, y)