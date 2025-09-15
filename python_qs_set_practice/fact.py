# factorial of a number 

a = int(input("Enter Your value : "))
f = 1
for i in range(1,a+1):
    f = f * i
    i += 1
print(f"Factorial of {a} is : ",f)