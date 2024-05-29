xM, yM, xN, yN, a = [float(i) for i in input().split()]
xO = (xM + a * xN) / (1 + a)
yO = (yM + a * yN) / (1 + a)
print(f"{xO:0.2f} {yO:0.2f}")
