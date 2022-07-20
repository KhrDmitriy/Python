
def Coordinates(qvad):
    if (qvad == 1):
        print('x > 0 ; y > 0')
        return('x > 0 ; y > 0')
    if (qvad == 2):
        print('x < 0 ; y > 0')
        return('x < 0 ; y > 0')
    if (qvad == 3):
        print('x < 0 ; y < 0')
        return('x < 0 ; y < 0')
    if (qvad == 4):
        print('x > 0 ; y < 0')
        return('x > 0 ; y < 0')

Q = int(input ('Enter the quarter number - '))
Coordinates(Q)