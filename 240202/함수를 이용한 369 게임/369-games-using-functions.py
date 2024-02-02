def is369(i):
    s = str(i)
    if '3' in s:
        return True
    elif '6' in s:
        return True
    elif '9' in s:
        return True
    else:
        return False 
    
def is3be(i):
    return i %3 ==0




a,b = map(int,input().split())

cnt = 0 

for i in range(a,b+1):
    if is369(i) or is3be(i):
        cnt+=1 

print(cnt)