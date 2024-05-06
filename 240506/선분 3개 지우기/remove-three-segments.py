n= int(input())
line_list= [tuple(map(int,input().split())) for _ in range(n)]
cnt=0 

for i in range(n-2): #뺄것 고르기 
    for j in range(i+1,n-1):
        for k in range(j+1,n):

            cnt_list = [0]*(101) # 최대길이 101임... 주의 
            #순회
            for t in range(n):
                if t in [i,j,k]:
                    continue 
                
                a,b= line_list[t]
                #값 더하기 
                for y in range(a,b+1):
                    cnt_list[y] += 1
            if max(cnt_list) <= 1 :
                cnt +=1

print(cnt)