n= int(input())

arr= [[0 for _ in range(n)]
        for _ in range(n)]

num =1

for j in range(n-1,-1,-1):
    
    #if (j%(n-1)) %2==0:#열의 값을. 열 마지막 값으로 나눈 값이 짝수이면 
    #if ((n-1)%j )%2 ==0: # 0으로 나누게 돼서 안됨.. 
    
    if (n-1 - j ) %2 ==0 : # 전체열 길이에서 해당열의 차가 짝수이면 
        for i in range(n-1,-1,-1):
            arr[i][j] = num
            num +=1
    else:
        for i in range(n):
            arr[i][j] = num
            num +=1

#출력
for i in arr:
    for k in i:
        print(k,end=" ")
    print()