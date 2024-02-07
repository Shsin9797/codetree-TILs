def f(arr):
    for i in range(len(arr)):
        if arr[i]%2 ==0:
            arr[i] = arr[i]//2
        


n= int(input())
_list = list(map(int,input().split()))
f(_list)
print(*_list)