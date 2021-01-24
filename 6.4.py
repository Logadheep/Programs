#4.Fibonacci series
#Get the number of integers required
x = int(input("Number of terms :"))
a = 0
b = 1
print(a)
print(b)
#^^ first 2 numbers/terms
for i in range(x):
    c = a + b           #adding preceeding numbers
    print(c)            #printing the sum
    a = b               #interchanging the values
    b = c
