# n = int(input())
# i = 1
# while n != i:
#     n = n / i
#     i += 1
# print(i)

# f = 1
# n = int(input())
# for i in range(1, 2001):
#     f = f * i
#     if (f == n):
#         print(i)
#     break


# lst1 = []
# lst = []
#
# n = 1
# for el1 in list(range(1, 2001)):
#     n *= el1
#     lst1.append(el1)

# print(f"{lst1}\n{lst}")

# n = int(input())
#
# # i = 1
# # for el in range(1, 40004):
# #     i *= el
# #     if n == i:
# #         print(el)
# #         break

import sys
sys.set_int_max_str_digits(6000)

n = int(input())
i = 1
for el in range(1, 2001):
    i = i * el
    if n == i:
        print(el)
        break


