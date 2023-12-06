xC, yC = [int(i) for i in input().split()]
xA, yA = [int(i) for i in input().split()]
xB, yB = [int(i) for i in input().split()]

a = (xC-xA) * (yB-yA) == (yC-yA) * (xB-xA)
b = (xB-xA) * (xC-xA) + (yB-yA) * (yC-yA) >= 0
c = 0 <= (xC-xA) * (xB-xA) + (yC-yA) * (yB-yA) <= (xB-xA) * (xB-xA) + (yB-yA) * (yB-yA)

if a:
    print("YES")
else:
    print("NO")
if a and b:
    print("YES")
else:
    print("NO")
if a and c:
    print("YES")
else:
    print("NO")

