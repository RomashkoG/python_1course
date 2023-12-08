a, b, c, d = [int(el) for el in input().split()]
num1 = []

if a > b:
    a,b = b,a
if c > d:
    c,d = d,c

for i in range(a, b+1):
    for j in range(c, d+1):
        if i*j not in num1:
            num1.append(i*j)

print(len(num1))
