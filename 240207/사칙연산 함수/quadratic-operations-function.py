def checkMun(x):
    if x in ['+','-','/','*']:
        return True     
    else:
        return False
    

def plus(x,y):
    return x+y

def minus(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x//y


x,m,y= input().split()
x,y = int(x),int(y)

if not checkMun(m):
    print('False')
else:
    print(f"{x} {m} {y} = ",end="")

    if m =='+':
        print(plus(x,y))
    elif m=='-':
        print(minus(x,y))
    elif m=='/':
        print(divide(x,y))
    elif m == '*':
        print(multiply(x,y))