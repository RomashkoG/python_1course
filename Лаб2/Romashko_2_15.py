a, b, c = [int(i) for i in input().split()]
D = (b**2) - (4 * a * c)

if D < 0:
    print("No roots")
elif D == 0:
    x = -b / (2 * a)
    print("One root:", x)
elif D > 0:
    x1 = (-b + (D**0.5)) / (2 * a)
    x2 = (-b - (D**0.5)) / (2 * a)
    print("Two roots:", min(x1, x2), max(x1, x2))
