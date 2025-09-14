# Python Program to Display Powers of 2 Using Anonymous Function

n=int(input("Enter Your limit : "))

num_power = lambda x: 2 ** x

print(f"The Number 2 power of from 0 to {n-1}")

for i in range(n):
    print(f"2 ^ {i} : {num_power(i)}" )


