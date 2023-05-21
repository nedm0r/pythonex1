a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
evennumberslist = []
oddnumberslist = []

for i in a:
    if i%2==0:
        evennumberslist.append(i)
        evennumberslist.sort()
    else:
        oddnumberslist.append(i)
        oddnumberslist.sort()

print("The even numbers list:" + str(evennumberslist))
print("The odd numbers list:" + str(oddnumberslist))