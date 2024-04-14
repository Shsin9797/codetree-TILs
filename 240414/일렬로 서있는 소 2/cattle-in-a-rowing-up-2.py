n= int(input())
cowH= list(map(int,input().split()))
cnt =0

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if cowH[i] < cowH[j] or cowH[i] == cowH[j]:
                if cowH[j] < cowH[k] or cowH[j] == cowH[k]:
                    cnt +=1 

print(cnt)