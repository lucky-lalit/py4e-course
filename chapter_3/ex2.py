# # print('HEllo world')
# hour=input('Enter Hours: ')
# try:
#     hour=float(hour)
#     # print('checking hrs type',type(hour),hour)  
#     rate=input('Enter Rate: ')
#     rate=float(rate)


# # try:
# #     rate=int(rate)
# # except:
# #     print('please enter number')
# #     print(' type of rate',type(rate)) 


# # # print('checking hour and rate',type(hour),type(rate)
# # # try:
#     if(hour>40):

#             hour=hour-40
#         # print("Puspendras help",40*rate, 1.5*hour*rate )
#             print('pay: ',((40*rate)+(1.5*hour*rate)))

#     else:
#         # print('lalits help', hour*rate)
#             print('pay: ',hour*rate)
#     # # except:
#     # #     print("plese enter the number",rate)
#     # print(' bye world')
# except:
#     print('Error, please enter numeric input')


try:
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
except:
    print("Error, please enter numeric input")