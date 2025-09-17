import calendar

year = int(input("Enter Your Year(e.g , 2025)"))
month = int(input("Enter Your Month(e.g , 1 - 12 )"))

print("Your Calender is : ")

print(calendar.month(year, month))
