n= int(input())
li= {}
point=0  

for _ in range(n):
    x,d= input().split()
    x= int(x)
    if d  =="L":
        for i in range(point-1,point-x,-1):
            if li.get(i):
                li[i] +=1
            else:
                li[i] =1 
        point = i 
    elif d=="R" :
        for i in range(point+1,point+x+1):
            if li.get(i):
                li[i] +=1
            else:
                li[i] =1 
        point=i

#개수 세기 
cnt =0 
for i in li.keys():
    if li[i] >=2:
        cnt +=1

print(cnt)