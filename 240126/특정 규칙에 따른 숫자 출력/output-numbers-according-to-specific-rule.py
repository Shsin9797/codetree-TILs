n= int(input())
cnt =1
for i in range(n,0,-1):#행
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(i): 
        if cnt >9:
            cnt=1
        print(cnt,end=" ")
        cnt +=1
    print()