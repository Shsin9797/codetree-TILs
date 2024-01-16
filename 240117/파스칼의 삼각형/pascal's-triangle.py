n = int(input())


#여긴 행, 열이 바꾼상태로 적음.. 보통은 i 가 행인데 열이게 적음..
#바깥 for 문의 변수가 그대로 쓰여야 하기때문에 _로 안나타내고 문자로 나타냈다.
arr= [[0 for i in range(j+1)] for j in range(n)] #여기 주의 i range(1,j)아님 range(j+1)임  j도 range(n+1)아님

for i in range(n):#행 수
    for j in range(i+1): #열 수
        if j ==0 or j == i :
            arr[i][j]=1
        else:
            arr[i][j]= arr[i-1][j]+arr[i-1][j-1] 

#출력
for i in arr:
    print(*i)