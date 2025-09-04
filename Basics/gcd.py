print("Enter 1st value")
x=int(input())
print("Enter 2nd value")
y=int(input())
while(z!=0) :
    x=y
    y=z
    z=x%y

print("GCD is " + str(z))