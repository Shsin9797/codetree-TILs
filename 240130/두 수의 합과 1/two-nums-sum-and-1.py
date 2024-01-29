a,b = map(int,input().split())

Sum= a+b 
result=str(Sum)
cnt = 0 

for i in result:
    if i =='1':
        cnt +=1
    
print(cnt)