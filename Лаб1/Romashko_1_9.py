a, b, n = [int(d) for d in input().split()]
a = a * n
b = b * n
while b>100:
    a = a + b//100
    b = b%100
print(a, b)
