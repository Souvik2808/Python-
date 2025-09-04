arr = []
num=int(input("Enter Size of Array : "))
for i in range(num):
    ele = int(input("Enter Your Element : "))
    arr.append(ele)
print("Your array is : ", arr)

max=min=arr[0]

for i in arr:
    if(i > max):
        max = i 
    

    if(i < min):
        min = i

print(f"Your max element in array : {max}")
print(f"Your min element in array : {min}")