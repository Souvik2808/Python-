# 12. Python Program to Make a Simple Calculator

print("If you choose Addtion , then press 1 :")

print("If you choose Substraction , then press 2 :")

print("If you choose Multiplication , then press 3 :")

print("If you choose Division , then press 4 :")

ch = int(input("Enter Your Choice : "))

num1 = int(input("Enter Your 1st value : "))
num2 = int(input("Enter Your 2nd value : "))


if(ch == 1):
    print(f"{num1} + {num2} = ",num1+num2)

elif(ch == 2):
    print(f"{num1} - {num2} = ",num1-num2)

elif(ch == 3):
    print(f"{num1} * {num2} = ",num1*num2)

elif(ch == 4):
    if(num2 != 0):
        print(f"{num1} // {num2} = ",num1//num2)
    else:
        print("You can't Divided any digit by zero ")
else:
    print(f"You Entered this {ch}, so this number is invalid")
        

