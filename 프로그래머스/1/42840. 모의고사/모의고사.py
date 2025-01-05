def solution(answers):
    s1,s2,s3 = [1,2,3,4,5],[2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]
    c1,c2,c3= 0,0,0
    for i in range(len(answers)): #range 적는거 주의
        co= answers[i]
        if s1[i%len(s1)] == co:
            c1 +=1
        if s2[i%len(s2)] == co:
            c2 +=1
        if s3[i%len(s3)] == co:
            c3 +=1
    max_cnt = max([c1,c2,c3])
    
    answer = []
    if c1==max_cnt : 
        answer.append(1)
    if c2==max_cnt : 
        answer.append(2)
    if c3==max_cnt : 
        answer.append(3)
        
    return answer