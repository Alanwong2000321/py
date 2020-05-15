s = input()
n = int(input())
if(n>len(s)):
    n -= len(s)
s = s[n:] + s[:n]
print(s)