import sys
n=int(input())

people = list(map(int,input().split()))

min_sum= sys.maxsize

for spot in range(n): # 지점 선택
    sum_movement =0
    for j in range(n):
        sum_movement += abs(spot-j)*people[j]
    min_sum =min(min_sum,sum_movement)

print(min_sum)