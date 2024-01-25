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

print(cntEB,cntEE)