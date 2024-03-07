n= int(input())
pointer =0
orderList =[]
RANGE = 100000

#명령 입력받기 
for _ in range(n):
    x,d =input().split()
    x = int(x)

    if d == "L": #왼쪽, 흰색 
        left= pointer -x +1 # == 두개안쓰게 주의 
        right= pointer
        pointer = left # pointer 값 변경 주의 
    elif d=="R" : #오른쪽 ,검정
        left = pointer
        right= pointer +x -1
        pointer = right
    orderList.append([left,right,d])

white = [0 for _ in range(2*RANGE+2)] #200001 개 만들어져야함
black = [0 for _ in range(2*RANGE+2)]
OFFSET =RANGE

#명령 수행하기 
for l,r,d in orderList:
    l += OFFSET
    r += OFFSET

    if d== "L": #왼쪽, 흰색
        for i in range(l,r+1):
            white[i] =1
            black[i] =0
    elif d=="R" : #오른쪽 , 검정색 
        for i in range(l,r+1):
            white[i] =0
            black[i] =1


print(sum(white),sum(black))