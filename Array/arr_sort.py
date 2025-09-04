arr = []
num = int(input("Enter the size of the list : "))
for i in range (num):
    ele = int(input("Enter the Element : "))
    i += 1
    arr.append(ele)

print("Array is : ",arr)


# in build >>>>>>>>>

arr.sort()
print("After Sorting this array by in build function : ",arr)

# manual sorting >>>>>>

for i in range(num):
    for j in range(i+1, num):
        if(arr[i] > arr[j]):
            t = arr[i]
            arr[i] = arr[j]
            arr[j]= t

print("After Manual Sorting Result of this array is : ",  arr)