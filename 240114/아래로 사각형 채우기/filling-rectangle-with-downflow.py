n= int(input())

arr=[ [0 for _ in range(n)] 
      for _ in range(n)]

num =1

for j in range(n):#열
    for i in range(n):#행
        arr[i][j] = num
        num+=1


#출력
for k in arr:
    for j in k:
        print(j,end=" ")
    print()