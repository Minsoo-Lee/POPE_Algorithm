lst = [1, 5, 3, 2, 8, 9, 6, 4, 7]
print(lst)

for i in range(0, len(lst)):
    for j in range(i, 0, -1):
        if lst[j] < lst[j - 1]:
            lst[j], lst[j - 1] = lst[j - 1], lst[j]
    print(lst)
print(lst)