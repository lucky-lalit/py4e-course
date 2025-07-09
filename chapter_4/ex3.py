# Exercise 3: 
# Move the function call back to the bottom and move the definition of print_lyrics after the definition of 
# repeat_lyrics. What happens when you run this program?



def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print('Mera naam hai giyaan')
    print('Mera gala hai surila, meri awaz suun k log ho jate hai madhosh')

repeat_lyrics()