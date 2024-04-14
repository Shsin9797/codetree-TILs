# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
grid = [
    input().split()
    for _ in range(n)
]

# 이동 시에 행과 열이 전부 증가하도록
# 모든 쌍을 다 잡아봅니다.
cnt = 0
for i in range(1, n):
    for j in range(1, m):
        for k in range(i + 1, n - 1):
            for l in range(j + 1, m - 1):
                # 그 중 색깔이 전부 달라지는 경우에만 개수를 세줍니다.
                if grid[0][0] != grid[i][j] and \
                   grid[i][j] != grid[k][l] and \
                   grid[k][l] != grid[n - 1][m - 1]:
                    cnt += 1
                        
print(cnt)

'''R,C = map(int,input().split())
mat= [input().split() for _ in range(R)]

color1 = mat[0][0] 

cnt = 0 

for i in range(1,R-2): #행 
    for j in range(1,C-2): #열 

        if color1 != mat[i][j]:
            color2 = mat[i][j]
            #print(i,j,end=" >> ")
            
            for k in range(i+1,R-1):#행
                for t in range(j+1,C-1):#열

                    if color2 != mat[k][t]:
                        color3 = mat[k][t]
                        #print(k,t,end=" >> ")

                        if color3 != mat[R-1][C-1] :
                            cnt +=1
                            #print()

print(cnt)

'''

'''
10 10
B W B B W B W W W B 
B W B W B W W B W W 
W W W B W W B B W B 
B W B W W W W B B B 
B B B B W W W W B B 
W W W B B W W W B B 
B B B W B W B W W W 
W W B W W W W W W W 
B W B W B B W W W W 
B B W W W B W W B W 
'''


'''
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