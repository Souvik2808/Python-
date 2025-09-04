arr = []
num = int(input("Enter the Size of the List : "))
for i in range(num):
    ele = int(input("Enter Your Element of this list : "))
    arr.append(ele)

print("Your array : ",arr)

search = int(input("Enter Your Serach value : "))
for i in arr:
    if(i == search):
        print(f"Element to be found")
        exit()
print(f"Element not found..")