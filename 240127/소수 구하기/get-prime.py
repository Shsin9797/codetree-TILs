n= int(input())

# 1~n까지수 
for i in range(1,n+1):
    isSosu = True
    #i가 소수인지 확인 => 1과 자기자신만을 약수로,, 나머기로 나누어떨어지면 소수가 아님 
    
    
    """for j in range(2,n): # 여기 n 이라서 .. 그런듯 
        if i!=j and i%j == 0: # 왜 i!=j  조건 필수인지.. 없으면 왜 아무것도 안뜨는지 모르겠음 
            isSosu=False"""

    for j in range(2,i):
        if i%j ==0:
            isSosu =False 
    #소수면 i출력 
    if i!=1 and isSosu:
        print(i,end=" ")