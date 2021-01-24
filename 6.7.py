#7.Printing patterns
#*****
#****
#***
#**
#*
x = int(input())
#This can be done as simple as that
#You can also refer the 11th std cs book for answers
for i in range(x,-1,-1):
    for j in range(i):
        print("*" , end=" ")
    print(end = "\n")

