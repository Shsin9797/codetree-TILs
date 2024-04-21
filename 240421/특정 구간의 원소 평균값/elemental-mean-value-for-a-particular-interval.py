import statistics 

n= int(input())
arr= list(map(int,input().split()))

cnt = 0 
for i in range(n):
    for j in range(i,n):
        avg = statistics.mean(arr[i:j+1])
        for k in range(i,j+1):
            if avg == arr[k]:
                cnt +=1
                break

print(cnt)