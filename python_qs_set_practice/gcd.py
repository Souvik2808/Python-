# Python Program to Find HCF or GCD

y = int(input("Enter Your 2nd value : "))
x = int(input("Enter Your 1st value : "))
y = int(input("Enter Your 2nd value : "))

while y != 0:
    x, y = y, x % y

print("GCD is : "+str(x))