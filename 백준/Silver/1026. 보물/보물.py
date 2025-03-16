def min_S(N, A, B):
    A.sort()  # A는 오름차순 정렬
    B.sort(reverse=True)  # B는 내림차순 정렬

    S = sum(a * b for a, b in zip(A, B))
    return S

# 입력 받기
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 결과 출력
print(min_S(N, A, B))