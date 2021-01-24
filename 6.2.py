#2.Using if...else...elif statement check smallest of three numbers
x,y,z = input().split()
#split() splits the given input by the given string argument.The argument is " "
#by default
x = int(x)
y = int(y)
z = int(z)
#above statements convert string into integer
if x<y and x<z:
    print(x)
#if x is smallest
elif y<z and y<x:
    print(y)
#if y is smallest
elif z<x and z<y:
    print(z)
#if z is smallest
