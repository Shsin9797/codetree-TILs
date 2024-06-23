n=int(input())

li= [ list(map(int,input().split())) for _ in range(n)]

max_cnt = 0

for stone in range(1,4):
    cnt =0
    li_stone= [0,0,0,0]
    li_stone[stone] =1 

    for action in li : 
        c1,c2,op= action
        li_stone[c1],li_stone[c2] = li_stone[c2],li_stone[c1]
        cnt += li_stone[op]
    
    max_cnt = max(max_cnt,cnt)

print(max_cnt)