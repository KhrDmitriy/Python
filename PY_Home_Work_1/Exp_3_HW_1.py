
def FindQvart(x,y):
    if (x > 0) and (y > 0):
        print('1')
        return('1')
    elif (x < 0) and (y > 0):
        print('2')
        return('2')
    elif (x < 0) and (y < 0):
        print('3')
        return('3')
    elif (x > 0) and (y < 0):
        print('4')
        return('4')   
    else:
        print('0')
        return('0')
     
A = float(input ('Inpyt X coordinate - '))
B = float(input ('Inpyt Y coordinate - '))
FindQvart(A,B)
