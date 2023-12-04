n = int(input())
i = 0
i2 = 0
while i2<n:
    i +=1
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
        i2 += 1
        print(i, end=" ")