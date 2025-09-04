# duplicate element check in array .....

arr = []
num=int(input("Enter the array size : "))
for i in range(num):
    ele = int(input("Enter the array element : "))
    arr.append(ele)

print("Your array is : ",arr)


for i in range(num):
    for j in range(i+1, num):
        
        if(arr[i] == arr[j]):
            print(f"duplicate value found in array .")
            exit()

print(f"No duplicate value found in array .")
