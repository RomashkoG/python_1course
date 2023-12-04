n = int(input())
i = 1
i1 = 0
while True:
    i1 = i**3
    i += 1
    if i1 >= n:
        break
    print(i1, end=" ")