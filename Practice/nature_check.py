char = input("Enter any key : ")
if(char.isalpha()):
    print(f"User Press this {char}... So Your key nature is Alphabet")
elif(char.isdigit()):
        print(f"User Press this {char}... So Your key nature is Number")
elif(char.isspace()):
        print(f"User Press this {char}... So Your key nature is White Space Character")
else:
    print("User Entered Any Symboll....")
        