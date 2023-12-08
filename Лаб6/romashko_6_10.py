#https://www.eolymp.com/uk/submissions/15421550

a = str(input())
a1 = ""

for el in a:
 if el in "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm":
  a1+= el * 2
 else:
  a1 += el

print(a1)