arr= input()
while len(arr)>1:
    idx= int(input())
    if len(arr)<=idx:
        arr = arr[:-1]
    elif idx==0:
        arr= arr[1:]
    else:
        arr= arr[0:idx]+arr[idx+1:]
    print(arr)