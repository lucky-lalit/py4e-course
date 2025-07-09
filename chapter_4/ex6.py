# Exercise 6: 
# Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay 
# which takes two parameters (hours and rate)


def computepay(hours,rate):
    if(hours>40):
        extra_hours = hours-40
        # print("Puspendras help",40*rate, 1.5*hour*rate )
        return ((40 * rate)+(1.5 * extra_hours * rate))
    else:
        # print('lalits help', hour*rate)
        return hours * rate
    
try:
    hour=input('Enter Hours: ')
    hour=float(hour)
    rate=input('Enter Rate: ')
    rate=float(rate)
    # print('checking hour and rate',type(hour),type(rate))
    pay = computepay(hour,rate)
    print('pay: ',pay)
except:
    print("Error, please enter numeric input")