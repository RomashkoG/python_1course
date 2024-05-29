n = int(input())
num = [float(el) for el in input().split()]
num1 = []

if n != len(num):
    raise ValueError

for i in num:
    if i > 0:
        num1.append(i)

if len(num1) > 0:
    print("%.2f" % (sum(num1)/len(num1)))
else:
    print("Not Found")