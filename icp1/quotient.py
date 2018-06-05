import math
math.pi

num1String = input('Please enter an integer: ')
num2String = input('Please enter a second integer: ')

num1 = int(num1String)
num2 = int(num2String)

quotient = num1 // num2
remainder = num1 % num2
print("the quotient is :", quotient)
print("the remainder is :", remainder)