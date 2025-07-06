hour=input('Enter Hours: ')
hour=float(hour)
rate=input('Enter Rate: ')
rate=float(rate)
# print('checking hour and rate',type(hour),type(rate))
if(hour>40):
    hour=hour-40
    # print("Puspendras help",40*rate, 1.5*hour*rate )
    print ('pay: ',((40*rate)+(1.5*hour*rate)))
else:
    # print('lalits help', hour*rate)
    print('pay: ',hour*rate)