x,y = map(int,input().split())

def isPal(num):
    numList= list(str(num))
    length=len(numList)
    for i in range(length//2):
        if numList[i] != numList[length-i-1]:
            return False
    return True 

cnt = 0 
for i in range(x,y+1):
    if isPal(i):
        cnt +=1

print(cnt)