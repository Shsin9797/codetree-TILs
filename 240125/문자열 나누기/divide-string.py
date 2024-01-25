n= int(input())

arr=input().split()
b=  "".join(arr)

cnt =1
for i in b:
    if cnt%5 !=0:
        print(i,end="")
    else:
        print(i)
    cnt+=1