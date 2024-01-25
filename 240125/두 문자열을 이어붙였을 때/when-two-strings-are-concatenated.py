A =input()
B= input()

AB = ""
BA =""

AB +=A
AB += B

BA +=B
BA +=A

# BA = "".join([B,A])
# AB ="".join([A,B])

isSame=True 

for i in range(len(AB)):
    if AB[i] != BA[i]:
        isSame=False

if isSame:
    print('true')
else:
    print('false')