n = int(input())
i = 0
for el in range(10, 100):
    s_el = (el % 10) + (el // 10)
    s_eln = 0
    for el2 in str(el*n):
        el2 = int(el2)
        s_eln += el2
    if s_el == s_eln:
        i += 1
print(i)