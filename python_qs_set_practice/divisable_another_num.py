# Python Program to Find Numbers Divisible by Another Number

start_value = int(input("Enter Your Starting Value : "))
end_value = int(input("Enter Your Ending value : "))
divisor = int(input("Enter Your Divisor Value : "))

for i in range(start_value, end_value + 1):
    if(i % divisor == 0):
        print(i)

