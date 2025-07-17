# Exercise 5:
# Slicing strings
# Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence: 0.8475'
# Use find and string slicing to extract the portion of the string after the colon character and then use the float 
# function to convert the extracted string into a floating point number

str1= 'X-DSPAM-Confidence: 0.8475'
str2 = 'alpha-beta-gamma: 1.789'
str3 = ': -99.99999'
str4 = 'X-DSPAM-Confidence :  0.8475 '
str5 = 'alpha-beta-gamma :  1.789 '
str6 = ' :  -99.99999 '
str7= 'X-DSPAM-Confidence:0.8475 '
str8 = 'alpha-beta-gamma:1.789 '
str9 = ':-99.99999 '
# print(str.find(':'))
# answer = (str[20:])
# print(answer)
# print(type(answer))
# final = float(answer)
# print(type(final))
def convert_into_decimal(str):
    position = str.find(':')
    answer = str[position + 1:]
    # print(float(answer))
    return float(answer)

print(convert_into_decimal(str1))
print(convert_into_decimal(str2))
print(convert_into_decimal(str3))
print(convert_into_decimal(str4))
print(convert_into_decimal(str5))
print(convert_into_decimal(str6))
print(convert_into_decimal(str7))
print(convert_into_decimal(str8))
print(convert_into_decimal(str9))


