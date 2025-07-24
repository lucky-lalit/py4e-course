# import math
# x = math.sqrt(4)
# print(x)
# print(x)


# x = 7

# def foo(x):
#     x = x + 3
#     print('Inside foo',x)
#     pass

# foo(x)
# print('outside foo',x)
# foo(x)

#def computepay(h, r):
 #   return 42.37

#hrs = input("Enter Hours:")
#p = computepay(10, 20)
#print("Pay", p)
def computepay(h,r):
    hrs=input('Enter Hours: ')
    hrs=float(hrs)
    rate=input('Enter Rate: ')
    r=float(r)
    if(h>40):
        extra_hours = h-40
        # print("Puspendras help",40*rate, 1.5*hour*rate )
        return ((40 * r)+(1.5 * extra_hours * r))
    else:
        # print('lalits help', hour*rate)
        return h * r
    

    hrs=input('Enter Hours: ')
    hrs=float(hrs)
    rate=input('Enter Rate: ')
    r=float(r)
    # print('checking hour and rate',type(hour),type(rate))
p = computepay(h,r)
print('pay',p)
    #return 42.37

   # print("Error, please enter numeric input")

    