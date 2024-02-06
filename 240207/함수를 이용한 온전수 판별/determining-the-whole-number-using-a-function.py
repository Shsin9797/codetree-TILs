def na2(x):
    return x%2==0

def five(x):
    return x%10 ==5

def na3no9(x):
    return x%3==0 and x%9 !=0

def isOn(x):
    if na2(x):
        return False
    elif five(x):
        return False
    elif na3no9(x):
        return False
    return True

a,b= map(int,input().split())

cnt =0 

for i in range(a,b+1):
    if isOn(i):
        cnt+=1

print(cnt)