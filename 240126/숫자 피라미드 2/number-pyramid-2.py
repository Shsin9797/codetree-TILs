n= int(input())

cnt =1
for i in range(n):
    for j in range(i+1): # i 가 0부터 시작함에 주의... 
        print(cnt,end=" ")
        cnt +=1
    print()