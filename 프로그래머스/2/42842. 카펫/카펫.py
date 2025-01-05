def solution(brown, yellow):
    i=1
    while True:
        # yellow 약수 되는거 찾기 
        a= i 
        b = yellow //a
        if a*b == yellow:    
            # 각각에 +2 해서 곱하면 b +y 되는지 확인 하고 되면 break
            if (a+2)*(b+2) == brown+yellow :
                break
        i+=1 
        
    a,b= max(a,b), min(a,b)
    answer = [a+2,b+2]
    return answer