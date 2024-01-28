arr= input()

print(arr)
for i in range(len(arr)):
    arr = arr[-1]+arr[:-1]
    print(arr)