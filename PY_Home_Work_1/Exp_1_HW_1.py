
# Первый вариант.

def weekend_day(day):
    if day == 6:
        print("YES, weekend")
    elif day == 7:
        print("YES, weekend")
    else:
        print("NOttt")

N = int(input ('Enter the number of the day of the week - '))
weekend_day(N)



# Второй вариант.

def weekend_day(day):
    if day==6 or day==7:
        print("YES, weekend")
    else:
        print("NOttt")
N = int(input ('Enter the number of the day of the week - '))
weekend_day(N)