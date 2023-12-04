n = int(input())
num = [int(el) for el in input().split()]
n1 = int(input())
num1 = [int(el) for el in input().split()]
num2 = []

if n != len(num) or n1 != len(num1):
    raise ValueError

for i in num:
    if i not in num1:
        num2.append(i)

num2_s = ""
for i in num2:
    num2_s += str(i) + " "

print(f"{len(num2)}\n{num2_s}")
