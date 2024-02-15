n= int(input())
arr = list(map(int,input().split()))
"""
리스트는 복사(대입) 될때 주소값 복사되는거라.. 슬라이싱으로 복사해줘야함... 
arr.sort()
arr1= arr
print(arr)
arr.sort(reverse=True)
arr2 = arr
"""

arr.sort()
arr1= arr[::]
arr2 = arr[::-1]

maxA = arr1[0]+arr2[0]
for e1, e2 in zip(arr1,arr2):
    if e1 + e2 > maxA:
        maxA = e1+e2

print(maxA)