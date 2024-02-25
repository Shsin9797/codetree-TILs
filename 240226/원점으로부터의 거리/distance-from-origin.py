cnt =0 

class Spot:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        global cnt
        cnt +=1
        self.cnt =cnt

n= int(input())
spotLi =[]
for _ in range(n):
    #x,y = 
    spotLi.append(Spot(*map(int,input().split())))

spotLi.sort(key= lambda j: (j.x+j.y,j.cnt))

for k in spotLi:
    print(k.cnt)