a = input("Enter a list of numbers, separated by spaces: ")
inplist =(a).split()  
numbersA = [int(i) for i in inplist]
print(numbersA[0], numbersA[-1])