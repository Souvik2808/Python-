# Count Negative or Positive or zero values while -1 is encountered :

negative=positive=zeroes = 0
print("Enter -1 for exit...")
while(1):
    num = int(input("Enter any number : "))
    if(num == -1):
        break
    if(num == 0):
        zeroes = zeroes + 1
    elif(num>0):
        positive = positive+1
    else:
        negative = negative+1

print("Count of positive numbers entered : ",positive)
print("Count of negative numbers entered : ",negative)
print("Count of Zeroes numbers entered : ",zeroes)