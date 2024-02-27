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
        totalMin +=1
        C +=1

        if A==a and B==b and C==c:
            break

        if C >= 60:
            B +=1
            C =0
        
        if B >= 24 :
            A +=1
            B=0
    print(totalMin)