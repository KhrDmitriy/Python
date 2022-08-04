
def factor(n):
    arr = list()
    i = 2
    while n / i >= 1:
        if n % i == 0:
            arr.append(i)
            n /= i
        else:
            i += 1
    return arr

num = int(input('Целое число: '))
print(factor(num))