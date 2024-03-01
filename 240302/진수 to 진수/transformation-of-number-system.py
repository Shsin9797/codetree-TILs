a,b =map(int,input().split())
n=input()
num=0
for i in range(len(n)):
    num = num*a + int(n[i])

li=[]
while True:
    if num <b:
        li.append(num)
        break
    
    li.append(num%b)
    num //=b

print(*li[::-1],sep="")