#sum of all natural Numbers :

n = int(input("Enter Your Limit Of Natural Numbers : "))
s = 0
for i in range(1,n+1):
    s = s+i
print(f"Sum of all natural Numbers for this limit {n} : ",s)