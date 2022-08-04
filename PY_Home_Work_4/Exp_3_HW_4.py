
# 1 вариант

# list_2 = ['Ivan', 'Dmitriy', 'Petr', 'Ivan', 'Leonid', 'Nikolay', 'Petr', 'Anatoliy']

# dic_elem = {}

# for i in list_2:
#     if i not in dic_elem:
#         dic_elem[i] = 1
#     else:
#         dic_elem[i] += 1

# arr = list()

# for i in dic_elem:
#     if dic_elem[i] == 1:
#         arr.append(i)
# print(arr)


# 2 вариант

lst = [45, -10, 23, 2, 45, -10, 1, 45]

d = {}
for i in lst:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1

arr = []
for i in d:
    if d[i] == 1:
        arr.append(i)
print(arr)



