A= input()
after =""

now= A[0]
after += now
cnt =0
for elem in A:
    if elem==now:
        cnt +=1 
    else:  
        after +=str(cnt)
        after += elem 
        cnt=1
        now = elem
after += str(cnt)

#출력 
print(len(after))
print(after)