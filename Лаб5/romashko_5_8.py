n = int(input())
num = [int(el) for el in input().split()]

if n != len(num):
    raise ValueError

print(min(num))