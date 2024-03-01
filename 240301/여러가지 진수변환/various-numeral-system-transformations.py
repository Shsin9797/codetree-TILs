n,b =map(int,input().split())

li = []
while True:
    if n<b:
        li.append(n)
        break
    
    li.append(n%b)
    n //=b

print(*li[::-1],sep="")