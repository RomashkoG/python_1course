l_num = []
while True:
    num = int(input())
    if num == 0:
        break
    else:
     l_num.append(num)

print(sum(int(i) for i in l_num if i % 2 == 0))