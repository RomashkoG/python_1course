a, b, c, d, f = [float(d) for d in input().split()]
p1 = (a+b+f)/2
p2 = (c+d+f)/2
s1 = (p1*(p1-a)*(p1-b)*(p1-f))**0.5
s2 = (p2*(p2-c)*(p2-d)*(p2-f))**0.5
s = s1+s2
print(f"{s:0.4f}")



 
