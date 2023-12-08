#https://www.eolymp.com/uk/submissions/15421606

a = str(input())
k = int(input())
a1 = ""

for el in a:
    n = chr((ord(el) - k - ord('A')) % 26 + ord('A'))
    a1 += n

print(a1)