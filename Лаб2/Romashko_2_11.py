n = int(input())
condition = 0
if n % 2 == 0 and n < 0 and n % 3 == 0:
    print("NO")
elif n % 2 == 0 or n < 0 and n % 3 == 0:
    print("YES")
else:
    print("NO")
