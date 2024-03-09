n= int(input())

arr =[] 
#일단 입력받기 
for _ in range(n):
    num = int(input())
    arr.append(num)

#연속 부분수열 ~ 부호동일한거 최대길이 찾기
cnt =0 
cntList=[]
for i in range(len(arr)):
    if i==0 or (arr[i-1] >0 and arr[i]<0) or (arr[i-1]<0 and arr[i]>0):
        cntList.append(cnt)
        cnt =1
    else:
        cnt+=1


print(max(cntList))