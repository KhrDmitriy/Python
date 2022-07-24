
def Factorial(Num):
    fact=1
    for i in range(1, Num+1):
        fact=fact*i
    print(fact)
    return fact
N=int(input('Введите число / Enter a number -->   '))
print('Entered number --> ',N)
Factorial(N)



# Второй вариант (набор произведений)

def MultiplicationOfANumber(Num):
    x=1
    for i in range(1, Num+1):
        x=x*i
        print(x)
    return(x)
N=int(input('Введите число / Enter a number -->   '))
print('Entered number --> ',N)

MultiplicationOfANumber(N)
