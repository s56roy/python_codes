a = input('Enter the First Number:')
b = input('Enter the Second Number:')

# The entered value 10 is a string, not a number. To convert this into a number we can use int() or float() functions.

sum = float(a)+float(b)

print(sum)

print('The sum of {0} and {1} is {2}'.format(a, b, sum))

print('This is output to the screen')

print ('this is output to the screen')

print ('The Sum of a & b is', sum)

print('The sum is %.1f' %(float(input('Enter again the first number: '))+float(input('Enter again the second number: '))))

print(1,2,3,4)
# Output: 1 2 3 4

print(1,2,3,4,sep='*')
# Output: 1*2*3*4

print(1,2,3,4,sep='#',end='&')
# Output: 1#2#3#4&

print('I love {0} and {1}'.format('bread','butter'))
# Output: I love bread and butter

print('I love {1} and {0}'.format('bread','butter'))
# Output: I love butter and bread

print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'John'))
# Hello John, Goodmorning

x = 12.3456789
print('The value of x is %3.2f' %x)
# The value of x is 12.35

print('The value of x is %3.4f' %x)
# The value of x is 12.3457

import math
print(math.pi)

from math import pi
pi
