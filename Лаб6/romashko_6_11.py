#https://www.eolymp.com/uk/submissions/15421566

a = str(input())
b = 0

for el in "qwertyuiopasdfghjklzxcvbnm":
    if el in a:
        b += 1
        break
for el in "QWERTYUIOPASDFGHJKLZXCVBNM":
    if el in a:
        b += 1
        break
for el in "1234567890":
    if el in a:
        b += 1
        break
for el in "!\"#$%&'()*+":
    if el in a:
        b += 1
        break
if len(a) >= 8:
    b += 1

print(b)