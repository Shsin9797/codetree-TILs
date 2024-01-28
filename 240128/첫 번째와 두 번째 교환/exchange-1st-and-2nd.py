arr= list(input())

f= arr[0]
s= arr[1]

for i in range(len(arr)):
    if arr[i] ==f:
        arr[i] =s 
    elif arr[i]==s : 
        arr[i] = f

print("".join(arr))