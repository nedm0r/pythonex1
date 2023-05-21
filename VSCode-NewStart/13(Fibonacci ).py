usernum = int(input("Input the number for the Fibonacci generator: "))


def FibFunc(usernum):
    x0 = 1
    x1 = 1
    fiblist = []
    for i in range(usernum):
     fiblist.append(x0)
     x0,x1 = x1,x0 + x1

    return (fiblist)

print(FibFunc(usernum))
