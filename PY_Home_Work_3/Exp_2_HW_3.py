

spisok = [2, 3, 4, 5, 6, 7, 8]

def multiply_el(lst):
    length = len(lst)
    new_lst = []
    for i in range(length // 2):
        new_lst.append(lst[i] * lst[-1- i])
    if length % 2 != 0:
        new_lst.append((lst[length // 2]) ** 2)
    print(new_lst)
multiply_el(spisok)








