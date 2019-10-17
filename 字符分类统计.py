a = input()
letter = 0#英文
digit = 0#数字
other = 0#其他
for b in a:
    if 48 <= ord(b) <= 57:
        digit += 1
    elif 65 <= ord(b) <= 90 or 97 <= ord(b) <= 122:
        letter += 1
    else:
        other += 1   
print('letter:%d' % letter)
print('digit:%d' % digit)
print('other:%d' % other)