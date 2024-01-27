n= int(input())

cnt = ord("A")

for i in range(n): #행
    for j in range(0,i+1): #열 i 는 0부터 시작함에 주의
        print(chr(cnt),end="")
        cnt += 1
        if cnt > ord("Z"):
            cnt = ord("A")
    print()

# 알파벳 다시 돌아가서 A 부터해야함에 주의