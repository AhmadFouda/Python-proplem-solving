#### the standard form ==> ax^2 + bx + c = 0 #####
import cmath
a = float(input('please enter the coefficient of X^2: '))
b = float(input('please enter the coefficient of X: '))
c = float(input('please enter the coefficient of C: '))
d = b ** 2 - 4 * a * c
root1 = (-b - cmath.sqrt(d)) / (2 * a)
root2 = (-b + cmath.sqrt(d)) / (2 * a)
print(f'the root1 is: {root1}')
print(f'the root1 is: {root2}')
