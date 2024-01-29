li = []
cnt = 0
while True:
    a= input()# 받는걸 반복문 안에 넣었어야했음 
    cnt += 1 
    if a =='0':
        break
    
    if cnt%2 ==1:
        li.append(a)

print(len(li))
print(*li,sep="\n")