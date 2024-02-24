class Person:
    def __init__(self,n,h,w):
        self.n=n
        self.h=h
        self.w=w

n=int(input())
#저장
people =[]
for _ in range(n):
    name, height, weight = input().split()
    height =int(height)
    weight=int(weight)
    p = Person(name,height,weight)
    people.append(p)

people.sort(key=lambda x:x.h)

#출력
for p in people:
    print(p.n,p.h,p.w)