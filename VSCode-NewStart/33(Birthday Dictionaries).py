import json

def printBirth(jsonfile):
 with open(str(jsonfile)) as f:
    data1 = json.loads(f.read())
 
 input1 = input("Welcome to the birth dictionary! Input a name : ")

 
 if input1 in data1:
    print("The birth of " + input1 + " is on " + data1[input1])
 else:
    print("No name in the dictionary")
 input2 = input("Enter a data about new person: ")

 with open(jsonfile, 'r+') as f:
    newdata = list(input2.split(","))
    data1[newdata[0]] = newdata[1]
    json.dump(data1,f)

printBirth("34.json")



