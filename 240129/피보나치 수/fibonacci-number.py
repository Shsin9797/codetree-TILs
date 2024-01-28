# DP 테이블 정의: F[i] : = F[1]부터 F[i-1]까지의 수를 더한값  
# 초깃값 정의 F[1] =1, F[2]=1 , F[3]=2
# 점화식 F[i]= F[i-1]+(i-1)

n=int(input())
F=[0 for _ in range(n+1)]
F[1]=1
F[2]=1
if n>2:
    for i in range(3,n+1):
        F[i] = F[i-1]+(i-1)
print(F[n])