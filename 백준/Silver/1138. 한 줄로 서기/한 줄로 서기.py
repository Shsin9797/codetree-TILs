# 입력 받기
N = int(input())  # 사람의 수
info = list(map(int, input().split()))  # 각 사람이 기억하는 정보

# 결과를 저장할 리스트 (N개의 빈 자리)
line = [0] * N  

# 1부터 N까지 작은 사람부터 배치
for height in range(1, N + 1):
    count = info[height - 1]  # 왼쪽에 있어야 하는 키 큰 사람 수
    position = 0  # 현재 배치할 위치

    # 빈 자리(0)를 하나씩 세면서 원하는 위치 찾기
    for i in range(N):
        if line[i] == 0:  # 빈 자리 발견
            if count == 0:
                line[i] = height  # 배치 완료
                break
            count -= 1  # 왼쪽에서 키 큰 사람이 지나감

# 결과 출력
print(*line)
