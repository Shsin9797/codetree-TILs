import sys 

n= int(input())

arr= list(map(int,input().split()))

min_cha= sys.maxsize 

for i in range(n): #두배 
    arr[i] *= 2

    #제거 
    for j in range(n):
        cha =0 
        arr2 = [elem for k,elem in enumerate(arr) if k!=j]
        
        #차의 합 구하기
        for t in range(n-2):
            cha += abs(arr2[t+1]-arr2[t])
        min_cha= min(min_cha,cha) # 얘 위치 주의 

    #복구
    arr[i] //= 2

print(min_cha)