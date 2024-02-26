cnt =1

class Student:
    def __init__(self,height,weight):
        self.h=height
        self.w= weight
        
        global cnt
        self.n= cnt
        cnt +=1

n= int(input())
sList =[]
for _ in range(n):
    h,w = map(int,input().split())
    sList.append(Student(h,w))

sList.sort(key= lambda x : (x.h,-x.w))

for s in sList:
    print(s.h,s.w,s.n)