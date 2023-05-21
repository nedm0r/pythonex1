usernum = int(input("Enter your number: "))
divisorslist = []
rangelist = list(range(1,usernum+1))

for i in rangelist:
    if usernum%i == 0:
        divisorslist.append(i)

print("Divisors of your number is:" + str(divisorslist))



