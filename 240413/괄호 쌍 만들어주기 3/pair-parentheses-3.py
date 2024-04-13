A= input()
n=len(A)
cnt = 0 

def start(i):
    global A
    cnt_close=0
    for k in range(i+1,n):
        if A[k] ==')':
            cnt_close +=1
    return cnt_close

for i in range(n):
    if A[i]=='(':
        cnt += start(i)

print(cnt)