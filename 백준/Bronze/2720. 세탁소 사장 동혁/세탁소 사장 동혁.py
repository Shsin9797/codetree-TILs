T = int(input())  
for _ in range(T):
    C = int(input())  # 거스름돈 (센트 단위)
    q = C // 25  # 25센트 (쿼터)
    C %= 25
    d = C // 10     # 10센트 (다임)
    C %= 10
    n = C // 5    # 5센트 (니켈)
    C %= 5
    p = C         # 1센트 (페니)
    print(q,d,n,p) 