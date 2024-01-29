li = []
cnt = 0
while True:
    a= input()# 받는걸 반복문 안에 넣었어야했음 
    
    if a =='0':
        break
    
    cnt += 1  # 더해주는 위치주의 

    if cnt%2 ==1:
        li.append(a)

print(cnt) #뭘 출력하는지 주의 
print(*li,sep="\n")