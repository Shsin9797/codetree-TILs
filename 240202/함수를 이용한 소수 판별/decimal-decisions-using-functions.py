def isSosu(i):
    if i >=2 :
        for k in range(2,i):
            if i%k==0:
                return False
    else:
        return False 
    
    return True 


def sumSosu(a,b):
    S=0 

    for i in range(a,b+1):
        if isSosu(i):
            S +=i
    return S

a,b = map(int,input().split())

print(sumSosu(a,b))