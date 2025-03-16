n = int(input())

a = 60 * 5  # 300초 (5분 버튼)
b = 60 * 1  # 60초 (1분 버튼)
c = 10      # 10초 버튼

if n % 10 != 0:
    print(-1)  # 10초 단위가 아니면 -1 출력
else:
    cnt_a = n // a  # 5분 버튼 횟수
    n %= a
    cnt_b = n // b  # 1분 버튼 횟수
    n %= b
    cnt_c = n // c  # 10초 버튼 횟수

    print(cnt_a, cnt_b, cnt_c)  # 각 버튼 횟수 출력
