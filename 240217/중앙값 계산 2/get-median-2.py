n= int(input())
numList= list(map(int,input().split())) #split 철자 주의... spilt 으로 i 를 먼저적어서 오류 
sortedList=[]


#순서대로 숫자를 읽다가 홀수 번째의 원소가 주어질 때마다 지금까지 입력받은 값의 중앙값을 출력
for i in range(n):
    sortedList.append(numList[i])
    if i%2 ==0:
        sortedList.sort()
        slen= (i+1)//2
        print(sortedList[slen],end=" ")