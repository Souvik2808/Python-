age = int(input("Enter Your Age : "))
if(age >= 18):
    print(f"Your age is {age}... So You are elegible for Vote...")
else:
     print(f"Your age is {age}... So You are not elegible for Vote...")
     left_age=18-age
     print(f"You have to wait for another {left_age} years to cast your vote.")