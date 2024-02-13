n= int(input())
arr=list(map(int,input().split())) #리스트로 바꾸는거 잊지말기

def f(idx): #0 ~ (idx) 값의 최소공배수 #idx-1 값의 공배수 아님.. idx 값의 공배수임 
    #종료조건 
    if idx ==0:
        return arr[idx] 
    elif idx ==1:
        a=arr[idx-1]
        b=arr[idx]

    else:            
        #재귀함수 :  (idx-1)에서 구한 공배수와 idx 값의 최소공배수 ##주의...  
        a= arr[idx]
        b= f(idx-1)

    if a>b:
        a,b= b,a #작은수를 a로 넘긴다 
    
    #공배수 구한다 
    i=b
    while True:
        if i%a ==0 and i%b==0:
            return i
        i+=1 # i 값 증가시키는거 까먹지말기..

print(f(n-1))