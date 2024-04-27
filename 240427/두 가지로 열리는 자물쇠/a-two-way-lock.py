n= int(input())

a1,b1,c1 =map(int,input().split())
a2,b2,c2 = map(int,input().split())

def inn(a1,a):
    #print('a1',a1,'a',a)
    a1 = a1-1

    if abs(a1-a) <= 2:
        return True 
    
    if a1 == n-1 :
        if a== 0 or a==1:
            return True 

    if a1 == 0 : 
        if a==(n-1) or a==(n-2) :
            return True
    
    if a1 == 1 : 
        if a == (n-1):
            return True

    if a1 == (n-2) :
        if a== 0 :
            return True
    ## 

    if a == n-1 :
        if a1== 0 or a1==1:
            return True 

    if a == 0 : 
        if a1==(n-1) or a1==(n-2) :
            return True
    
    if a == 1 : 
        if a1 == (n-1):
            return True

    if a == (n-2) :
        if a1 == 0 :
            return True

    return False


def able(a,b,c):
    # global a1,b1,c1,a2,b2,c2
    
    if inn(a1,a) and inn(b1,b) and inn(c1,c):
        return True

    if inn(a2,a) and inn(b2,b) and inn(c2,c):
        return True
    
    return False

cnt =0 

for i in range(n):
    for j in range(n):
        for k in range(n):
            
            if able(i,j,k):
                cnt +=1

print(cnt)