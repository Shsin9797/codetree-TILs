R,C = map(int,input().split())
mat= [input().split() for _ in range(R)]




total = 0 

while True:
    cntJump = 0
    x,y=0,0
    color = mat[y][x]
    #점프 해보기 
    while True:
        dy = y+1
        while True:
            dx = x+1 
            check_color = mat[dy][dx]
            if check_color != color :
                check_color= color 
                y = dy 
                x = dx 
                cntJump +=1 
    



'''
while True: 
    #격자 끝까지 이동해보기 
    cntJump = 0 
    for i in range(R):
        for j in range(C):
            temp= mat[i][j]
            if temp != color and y<i and x<j:
                y =i 
                x =j 
                color = mat[y][x]
                cntJump +=1
                break
    if cntJump == 2:
        total +=1 

print(total)
'''