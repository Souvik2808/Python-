    
num = int(input("Enter Your value : "))    
s = 0
n = num
while(num > 0):
    r = num % 10
    s = s + (r**3)
    num = num // 10
 
if(n == s ):
    print(f"{num} is Armstrong ")
else:
    print(f"{num} is not Armstrong")