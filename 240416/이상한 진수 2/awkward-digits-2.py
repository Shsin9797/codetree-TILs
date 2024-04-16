a =input()
li = [i for i in a ]
n= len(li)
Nli=[]

def getTen(semi):
    ten =0
    global n
    for i in range(n):
        ten= ten*2 + int(semi[i])
    return ten 


for i in range(n):
    semi = li[:]
    if semi[i] =='0': #기호처리 해주기..
        semi[i] ='1'
    else:
        semi[i] = '0' 
    Nli.append(getTen(semi))

print(max(Nli))