x1, x2, x3 = [int(i) for i in input().split()]
if x1 == x2 and x1 == x3 and x2 == x3:
    print("1")
elif x1 == x2 or x1 == x3 or x2 == x3:
    print("2")
else:
    print("3")
