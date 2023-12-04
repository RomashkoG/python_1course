n = int(input())
l_num = []
for _ in list(range(n)):
    num = int(input())
    l_num.append(num)

for el in l_num:
    if el % 2 == 0:
        print(f"{el} is even")
    else:
        print(f"{el} is odd")
