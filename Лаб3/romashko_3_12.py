n = int(input())
n1 = 0
r_n = 0
l = -1

while n != r_n:
    n = n + r_n
    n1 = n
    r_n = 0
    for i in str(n):
        r_n = r_n * 10 + n1 % 10
        n1 = n1 // 10
    l += 1
print(l)
