n = str(input())
n2 = 0
true = True

for el in n:
    el = int(el)
    if el % 2 == 0:
        n2 += el
        true = False

if true:
    n2 = n2 -1

print(n2)
