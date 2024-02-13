a,b,c = map(int,input().split())
target = str(a*b*c)
print(target)

def f(idx):# 0~ (idx-1) 번째까지 자리값을 더하여 반환 
    #종료조건
    if idx ==1: #idx 는 길이를 넣을거라.. 0이 안됨.. 0이면 0 반환해야함 
        return int(target[0])
    print(target[idx-1])
    #재귀호출 
    return f(idx-1)+int(target[idx-1])

print(f(len(target)))