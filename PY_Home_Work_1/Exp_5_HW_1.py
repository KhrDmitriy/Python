
def Sqrt(x1, y1, x2, y2):
    import math
    sqrt = math.sqrt((x2-x1) ** 2 + (y2-y1) ** 2 )
    print(sqrt)
    return(sqrt)
 
X1 = float(input('введите координату x1 '))
Y1 = float(input('введите координату y1 '))
X2 = float(input('введите координату x2 '))
Y2 = float(input('введите координату y2 '))

Sqrt(X1, Y1, X2, Y2)