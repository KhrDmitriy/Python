
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            expression1 = not(x or y or z)
            expression2 = not x and not y and not z
            print(f'{x} | {y} | {z}  =  {expression1 == expression2}')