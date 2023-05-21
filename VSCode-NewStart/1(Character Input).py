import datetime

current_year = datetime.datetime.now().year
name = input("Enter your name :")
age = int(input("Enter your age:"))
age100 = current_year - age + 100
print ("Your name is " + name + " and you will be 100 years old in " + str(age100))