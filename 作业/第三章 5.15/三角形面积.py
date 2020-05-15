x = int(input())
y = int(input())
z = int(input())
p=(x+y+z)/2
s=(p*(p-x)*(p-y)*(p-z))
print("%.2f"%(s**0.5))