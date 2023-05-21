userword = str(input("Enter the word: "))
revers = userword[::-1]
#revers = ''.join(reversed(userword))
print (revers)

if userword.lower()==revers.lower():
    print("The word is a polidrom")
else:
    print("No polidrom")