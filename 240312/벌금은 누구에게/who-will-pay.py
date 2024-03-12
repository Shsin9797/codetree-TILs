N,M,K =map(int,input().split())
fair = [0]*(N+1)
a= -1
for _ in range(M):
    num = int(input())
    fair[num] +=1
    if fair[num] >= K:
        a=num
        break
    
print(a)