n= int(input())
arr= list(map(int,input().split()))

cnt= len(arr)
money = [0 for _ in range(cnt)]

m = 0

for i in range(len(arr)): # money 의 인덱스 
    for j in range(i,len(arr)): #계산할값
        k= (arr[j]-arr[i]) #i,j 위치 주의 
        if m < k:
            m = k
    money[i] = m

print(max(money))