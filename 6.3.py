#3.Write a program to check if a number is positive or negative or zero
#Getting the input
x = int(input("Number is: "))
if x > 0:
    print("Positive")
#we know that a number less than 0 is negative and greater than zero is positive.
elif x < 0:
    print("Negative")
else:
    print("It is zero")
#if it is neither positive or negative it is of course a zero
