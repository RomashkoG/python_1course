n = int(input())
num = [int(el) for el in input().split()]
num1 = []

if n != len(num):
    raise ValueError

for i in num:
    if i not in num1:
        num1.append(i)

num1_s = ""
for i in num1:
    num1_s += str(i) + " "

print(num1_s)
