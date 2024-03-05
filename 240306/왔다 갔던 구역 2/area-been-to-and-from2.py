n= int(input())
li= {}
point = 0

for _ in range(n):
    x,d= input().split()
    x= int(x)
    if d  =="L": #끝점에 
        for i in range(point-1,point-x-1,-1):
            if li.get(i):
                li[i] +=1
            else:
                li[i] =1 
        point = i 
    elif d=="R" : #시작점에 
        for i in range(point,point+x):
            if li.get(i):
                li[i] +=1
            else:
                li[i] =1 
        point=i+1

#개수 세기 
cnt =0 
for i in li.keys():
    if li[i] >=2:
        cnt +=1

print(cnt)