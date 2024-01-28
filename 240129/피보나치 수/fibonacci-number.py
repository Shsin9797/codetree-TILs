# DP 테이블 정의: F[i] : = i번째 피보나치수
# 초깃값 정의 F[1] =1, F[2]=1 , F[3]=2
# 점화식 F[i]= F[i-1]+F[i-2]

n=int(input())
F=[0 for _ in range(n+1)]
F[1]=1

if n>1:
    F[2]=1
    for i in range(3,n+1):
        F[i] = F[i-1]+F[i-2]
print(F[n])