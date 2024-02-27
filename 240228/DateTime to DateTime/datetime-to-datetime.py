a,b,c =map(int,input().split())
A,B,C =11,11,11

totalMin =0
if A > a :
    print(-1)
elif A ==a and B>b :
    print(-1)
elif A ==a and B ==b and C > c:
    print(-1)
else:

    while True :


        if A==a and B==b and C==c: # 얘 위치 주의.. 맨처음에 체크하고 들어가야.. .시작시간이랑 끝나는 시간 같을때도 0 제대로 나옴 
            break

        if C >= 60:
            B +=1
            C =0
        
        if B >= 24 :
            A +=1
            B=0

        totalMin +=1
        C +=1
    print(totalMin)