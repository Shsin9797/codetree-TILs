n= int(input())
arr = input()
cnt =0 
for i in range(n-2):
    if arr[i]=='C':
        for j in range(i+1,n-1):
            if arr[j] =='O':
                for t in range(j+1,n):
                    if arr[t]=='W':
                        cnt +=1

print(cnt)