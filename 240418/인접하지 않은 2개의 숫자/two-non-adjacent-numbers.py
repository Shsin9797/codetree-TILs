import sys 

n= int(input())
arr = list(map(int,input().split()))

max_sum = - sys.maxsize
for i in range(n-1):
    for j in range(i+1,n):
        if abs(i-j) > 1 : 
            sum_num=arr[i]+arr[j]
            max_sum = max(max_sum,sum_num)

print(max_sum)