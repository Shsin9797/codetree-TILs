N,C,G,H = map(int,input().split())

class A:
    def __init__(self,a,b):
        self.a=a
        self.b=b

worker=[]

for _ in range(N):
    a,b= map(int,input().split())
    worker.append(A(a,b))

max_work=0
#온도 조정하면서 완전탐색
for t in range(1001): 
    
    workload=0
    for w in worker:
        if t < w.a :
            workload += C
        elif w.a <= t <= w.b:
            workload +=G
        elif t > w.b:
            workload += H
    
    max_work = max(max_work,workload)

print(max_work)