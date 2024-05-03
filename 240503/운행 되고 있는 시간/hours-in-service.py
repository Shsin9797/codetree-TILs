import sys 

n= int(input())
time= []
#개발자 시간 세팅
for _ in range(n):
    A,B =map(int,input().split())
    time.append((A,B))

max_time= -sys.maxsize
count0=[0]*1001
#개발자 한명씩 빼기 

for i in range(n):#뺄 개발자
    count=count0[::]
    #count =0 
    for j in range(n): #개발자 순회 
        if i ==j : 
            continue 
        s,e= time[j]
        #print(s,e)
        for t in range(s,e):
            count[t] = 1 # 플러스 하면 안됨.. 1로 고정되어야함  
        #print(count)
    #print()
    max_time = max(max_time,sum(count))

print(max_time)