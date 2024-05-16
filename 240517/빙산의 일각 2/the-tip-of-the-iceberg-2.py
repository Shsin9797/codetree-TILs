N=int(input())
H=[]

for _ in range(N):
    H.append(int(input()))



mh= max(H)
max_cnt=0 #매 수면 높이마다 cnt 는 초기화되고, cnt 중에 최대값을 찾아야함.. 

for water in range(mh+1):
    cnt=0 
    OX='X' # 얘도 초기세팅 x 로 해줘야함
    for i in range(N):
        bing = H[i] - water 
        if bing > 0 and OX=='X':
            cnt +=1 
            OX='O'
        
        if bing <= 0 and OX =='O':
            OX='X'
            
    max_cnt=max(cnt,max_cnt)

print(max_cnt)