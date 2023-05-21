a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newlist = []
newlist1 = []
for i in a:
 if (i<5):
  newlist.append(i)
  newlist.sort()

print(newlist) 



usernum = int(input("Enter your num for checking:"))
for x in a:
   if x<usernum:
    newlist1.append(x)
    newlist1.sort()
   else:
    print("No numbers")
print(newlist1)