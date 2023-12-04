n = str(input())
n2 = ""
a = 0

for i in n:
    if i != "1":
        n2 += i
        a = 1
    elif i == "1" and a == 1:
        n2 += i
    elif i == "1":
        pass

if n2 == "":
    n2 = "1"

for el in n2:
    if int(el) % 2 == 0:
        print(int(el)+1, end ="")
    else:
        print(int(el)-1, end="")
