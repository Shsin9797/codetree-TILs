class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    
studentList=[]
minIdx=0
minGrade=100
for i in range(5):
    name,grade=input().split()
    grade = int(grade)
    if grade < minGrade :
        minGrade = grade
        minIdx = i 
      
    studentList.append(Student(name,grade))

k = studentList[minIdx]
print(k.name,k.grade )