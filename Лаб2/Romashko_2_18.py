x, y, x1, y1, x2, y2 = [float(i) for i in input().split()]
if min(x1, x2) <= x <= max(x1, x2) and min(y1, y2) <= y <= max(y1, y2):
    print("1")
else:
    print("0")
