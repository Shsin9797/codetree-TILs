def solution(name):
    # 각 알파벳별 최소 조작 횟수 계산
    def get_change_count(char):
        # 위로 조작하는 횟수와 아래로 조작하는 횟수 중 최소값
        return min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

    n = len(name)
    answer = 0
    min_moves = n - 1  # 기본적으로 끝까지 가는 경우

    # 각 문자에 대해 변경에 필요한 조작 횟수 더하기
    for i, char in enumerate(name):
        answer += get_change_count(char)

        # 현재 위치 다음부터 연속된 A의 마지막 위치 찾기
        next_idx = i + 1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1

        # 현재까지 온 거리에서 뒤로 돌아가는 경우와
        # 처음으로 돌아갔다가 뒤에서부터 오는 경우 중 최소값 선택
        min_moves = min(min_moves,
                       # 현재 위치까지 왔다가 돌아가서 남은 부분 처리
                       i + i + n - next_idx,
                       # 뒤에서부터 처리하고 현재 위치까지 오기
                       n - next_idx + n - next_idx + i)

    # 상하 조작 횟수 + 좌우 이동 횟수
    return answer + min_moves