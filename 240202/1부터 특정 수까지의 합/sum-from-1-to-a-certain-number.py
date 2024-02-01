def nanuki(n):
    sumA=0
    for i in range(1,n+1):
        sumA+=i
    
    return sumA//10 



n= int(input())
a= nanuki(n)
print(a)