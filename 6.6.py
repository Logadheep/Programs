#6.Palindrome
#get input value
x = input()
y = x
x = x[::-1]
if y == x:
    print("Palindrome")
else:
    print("Not a palindrome")
