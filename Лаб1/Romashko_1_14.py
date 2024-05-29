x, y = [float(i) for i in input().split()]
a = ((2*x*y) / (((x**2) + (y**2))**0.5)) - (((x+y-1)**2) / (x*y))
print(f"{a:0.3f}")
