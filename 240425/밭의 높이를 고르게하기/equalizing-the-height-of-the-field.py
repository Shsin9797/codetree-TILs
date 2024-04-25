import sys

n,h,t = map(int,input().split())

li = list(map(int,input().split()))
min_cnt = sys.maxsize

for start in range(n):

    if start+t > n: #등호 있으면 안됨 
            break
    
    for end in range(start,start+t): #시작점끝점 정하기 

        cnt=0
        for i in range(start, end+1):# 해당인덱스범위의 밭의 높이를 h 로 바꾼다   
            cnt += abs(h-li[i])
            #print(cnt)

    if cnt !=0:
        min_cnt = min(min_cnt, cnt)

print(min_cnt)