import sys
n,b = map(int,input().split())

class Student():
    def __init__(self,p,s,i):
        self.price=p
        self.ship=s
        self.idx=i

student_list =[]  # 0 넣으면 안됨.. Student 객체 모임임 
max_student = -sys.maxsize
for i in range(n):
    p,s = map(int,input().split())
    student_list.append(Student(p,s,i))

#예산으로 선물 가능한 학생수 구하기 
def student_cnt(bud,student_list):
    student_list.sort(key= lambda x: (x.price+x.ship))
    cnt= 0
    i=0
    while bud > 0: 
        if i>= n:
            break
        bud -= student_list[i].price
        if bud >= 0: # 빼고 나서도 0 보다 큰경우에 cnt 증가시켜줘야함  
            cnt+=1
        i+=1
        
    return cnt 

#반값할인할 선물정하기
for i in range(n):
    student_list[i].price /= 2
    max_student= max(max_student,student_cnt(b,student_list[:]))
    student_list[i].price *= 2 #원상복구

print(max_student)