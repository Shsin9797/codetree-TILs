cnt =0
class Num:
    def __init__(self,n):
        self.n=n
        global cnt
        self.c=cnt
        cnt += 1
        self.cidx =0

n= int(input())
arr = list(map(int,input().split()))

nList=[]
for a in arr:
    nList.append(Num(a))

#정렬
nList.sort(key=lambda x: x.n)

#변경된 인덱스값 저장
for a in range(0,n):
    nList[a].cidx = a+1

#원래 순서대로 재정렬 
nList.sort(key=lambda x: x.c)

#변경된 인덱스값 출력
for a in nList:
    print(a.cidx,end=" ")