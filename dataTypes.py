import numpy as np

a = np.zeros((3, 3))
print(a)

# Soy un comentario!
print("Hello, World!")

# data types

# string
myString = "Hello, World!"
print(myString)

# numeric
myNumber = 5
print(type(myNumber))
print(myNumber)

myFloatNumber = 3.1416
print(type(myFloatNumber))
print(myFloatNumber)

myComplexNumber = complex(2.718, 3.1416)
print(type(myComplexNumber))
print("real value: " + str(myComplexNumber.real))
print("imaginary value: " + str(myComplexNumber.imag))
myComplexNumber.conjugate()

mylist = [1, 2, 3, 4, 5]

# Creación ambiente virtual
# https://cheatography.com/ilyes64/cheat-sheets/python-virtual-environments/
