n= input()
sip=0
for i in range(len(n)):
    sip = sip*2 + int(n[i])

sip *=17

li=[]
while True:
    if sip<2:
        li.append(sip)
        break
    
    li.append(sip%2)
    sip //=2

print(*li[::-1],sep="")