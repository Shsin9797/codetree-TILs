N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()  # A는 오름차순 정렬
B.sort(reverse=True)  # B는 내림차순 정렬

S = sum(a * b for a, b in zip(A, B))

# 결과 출력
print(S)