def isTwo(x):
    a= x[0]
    
    for i in range(len(x)):
        if x[i] != a:
            return True
    
    return False

A= input().split()

if isTwo(A):
    print("Yes")
else:
    print("No")