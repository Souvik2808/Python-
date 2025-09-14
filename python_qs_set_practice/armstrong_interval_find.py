# Python Program to Find Armstrong Numbers in a Given Interval

start = int(input("Enter Your Starting Value : "))
end = int(input("Enter Your Ending Value : "))

print(f"Armstrong numbers between {start} and {end} are:")
for num in range(start, end + 1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    if num == sum:
        print(num)






