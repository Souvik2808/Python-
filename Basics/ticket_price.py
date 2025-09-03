# Ticket Price Calculation Based on Age .....

age = int(input("Enter Your AGe : "))
if(age <= 0 ):
    print("Enter Valid Age ")
elif(18 >= age > 8):
    print("Your Ticket Price per head 20 rs")
else:
    print("Your Ticket Price per head 50 rs")