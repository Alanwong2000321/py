a = input()
b = a[:-1]
c = ''
for d in b:
    if 65 <= ord(d) < 90:
        c = c + chr(ord(d)+33)
    elif ord(d) == 90:
        c = c + "a"
    elif 97 <= ord(d) < 122:
        c = c + chr(ord(d)+1)
    elif ord(d) == 122:
        c = c + "a"
    elif 48 <= ord(d) <= 57:
        c = c + d
    else:
        c = c + d
print(c)
