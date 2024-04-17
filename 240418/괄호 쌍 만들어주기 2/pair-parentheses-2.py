A=input()
lA= len(A)
cnt=0

for i in range(lA-3): # 여기 2아니라 3빼줘야하는거 맞나..
    if A[i]=='('and A[i+1]=='(':
        for j in range(i+2,lA-1):
            if A[j]==')'and A[j+1] ==')':
                cnt+=1

print(cnt)

# # 변수 선언 및 입력
# string = input()
# n = len(string)

# # 모든 쌍을 다 잡아봅니다.
# cnt = 0
# for i in range(n - 1):
#     for j in range(i + 1, n - 1):
#         if string[i] == '(' and string[i + 1] == '(' and string[j] == ')' and string[j + 1] == ')':
#             cnt += 1
            
# print(cnt)