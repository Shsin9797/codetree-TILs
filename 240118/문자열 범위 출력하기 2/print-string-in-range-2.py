arr= input().strip()
le = int(input())
if le < len(arr):
    print(arr[len(arr):len(arr)-le-1:-1])
else:
    print(arr[::-1])