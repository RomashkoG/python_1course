#https://www.eolymp.com/uk/submissions/15421462

a = str(input())
lst = ["+", "-", "*", "/", "%"]
i = 0

r = [["**", "*"], ["//", "/"]]
for old, new in r:
    if old in a:
        a = a.replace(old, new)

for el in a:
    if el in lst:
        i+=1

print(i)