arr = input()
length = len(arr)

cntEE=0
cntEB=0
for i in range(length-1):
    if arr[i]=='e':
        if arr[i+1]=='b':
            cntEB +=1
        elif arr[i+1] == 'e':
            cntEE +=1

print(cntEE,cntEB) # 뭐먼저 적어야하는지 확인하기 & 콤마로 연결하면 스페이스 자동추가 되는군