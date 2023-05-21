usernum = int(input("Enter the nuymber: "))
if usernum%4 == 0:
    print("Your number is a multiple of 4")

elif usernum%2 == 0:
    print("Your number is a multiple of 2")
    
else:
    print(usernum, "is an odd number")   