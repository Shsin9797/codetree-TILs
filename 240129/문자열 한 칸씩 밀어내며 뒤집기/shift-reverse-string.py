arr,q= input().split()
q=int(q)

for i in range(q):
    num =int(input())
    if num ==1:
        arr = arr[1:]+arr[0]
    elif num ==2:
        arr=arr[-1]+arr[:-1]
    elif num ==3:
        arr= arr[::-1]

    print(arr)