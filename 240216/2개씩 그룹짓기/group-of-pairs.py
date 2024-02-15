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

""" 
해설 이해 잘 안되는 부분
 
이때 M+a >= b+m 
(M>=b, a>=m 이므로 )
a와 m 을 서로바꿔서 
[M,m],[a,b]로 만들면 M+m 과 a+b 값이 최댓값이 될수있습니다.  <<<<<< 
하지만 두 값 모두 M+a 보다는 같거나 작습니다. 


"""

arr.sort()
arr1= arr[::]
arr2 = arr[::-1]

maxA = arr1[0]+arr2[0]
for e1, e2 in zip(arr1,arr2):
    if e1 + e2 > maxA:
        maxA = e1+e2

print(maxA)