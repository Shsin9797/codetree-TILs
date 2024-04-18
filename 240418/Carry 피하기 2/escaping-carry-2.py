import sys
n= int(input())
arr = [input() for _ in range(n)]

max_sum = -sys.maxsize

#x='1234'
#lix = x[::-1]
#print(lix)

def isCarry(x,y,z):
    li =[0]*5

    lix= x[::-1]
    liy = y[::-1]
    liz= z[::-1] 

    lenx = len(x)
    leny= len(y)
    lenz =len(z)

    for i in range(5):
        sum_num=0
        if i < lenx:
            sum_num += int(lix[i])
        if i < leny:
            sum_num += int(liy[i])
        if i < lenz:
            sum_num += int(liz[i])
        
        if sum_num >=10:
            return True
    
    return False


carry = True

for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            fir,sec,thi = arr[i],arr[j],arr[k]
            sum_num=0
            if not isCarry(fir,sec,thi):
                sum_num = int(fir) + int(sec) + int(thi)
                max_sum = max(max_sum,sum_num)
                carry =False
                

            


if carry:
    print(-1)
else:    
    print(max_sum)