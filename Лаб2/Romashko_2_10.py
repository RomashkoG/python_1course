a = int(input())
if a<0:
     a = -a
b = a // 100
d = a % 10
if b>d:
    print(b)
elif d>b:
    print(d)
elif b==d:
    print("=")
