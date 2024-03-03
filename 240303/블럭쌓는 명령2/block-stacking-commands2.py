n,k = map(int,input().split())
block = [0 for _ in range(n+1)]
for _ in range(k):
    a,b =map(int,input().split())
    for i in range(a,b+1):
        block[i] +=1

print(max(block))