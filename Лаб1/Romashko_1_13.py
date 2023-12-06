x, y = [float(i) for i in input().split()]
a = (x**2 - 2*x*y + 4*y**2)/(x+5) + (3*x**2 - y**2)/(y-7)
print(f"{a:0.3f}")
