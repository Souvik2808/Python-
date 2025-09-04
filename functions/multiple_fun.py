# create a program that provides multiple functionality with iteartion


# User input for value check :

def take_user_input():
    num = int(input("Enter Your value : "))
    return(num)


# Even or Odd number check : 

def check_even_odd(num):
    result "Even Number" if num%2==0 else "Odd Number"
    print(f"{num} is {}")


# Prime Number Check : 

def prime_check(num):
    count = 0
    for i in range(1 , num+1):
        if(num%i == 0):
            count += 1

    if(count == 2):
        print(f"{num} is Prime number")
    else:
        print(f"{num} is not Prime number")


# Armstrong Number Check : 

 

