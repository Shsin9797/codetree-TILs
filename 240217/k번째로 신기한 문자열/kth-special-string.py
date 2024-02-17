n,k,T =input().split()
n,k= int(n),int(k)
T=list(T)
wordList= []

# T로 시작하는지 확인하는 함수
def isStartT(w):
    w= list(w) 
    isSame=True
    for i in range(len(T)):
        if T[i] != w[i]:
            isSame =False
            break
    return isSame
        
#입력 값들이 T로 시작하는지 확인 하고 리스트에 추가하는 구문
for _ in range(n):
    word= input()
    if isStartT(word):
        wordList.append(word)

#사전순으로 정리 
wordList.sort()

print(wordList[k-1])