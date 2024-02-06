def isSosu(x):
    if x<2:
        return False 

    for i in range(2,x):
        if x%i ==0:
            return False
    return True
    
def sumJa(x):
    #종료조건 
    if x <10 :
        return x
    #재귀호출 
    return sumJa(x//10)+ (x%10)    


a,b= map(int,input().split())

cnt =0 
for i in range(a,b+1): # 이하 라서 ..b 도 포함해야함 
    if isSosu(i) and sumJa(i)%2==0:
        cnt +=1

print(cnt)