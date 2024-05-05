N,K = map(int,input().split())
nums = [int(input()) for _ in range(N)]
#같은 번호 부여된 폭탄찾기 

max_num = -1 
print(nums)
for i in range(N):
    for j in range(i-3,i+4):# 특정 숫자를 적으면안되고... K 를 적어야죠.. 
        if i==j : #같은애면 안됨 
            continue # break 하면안됨..
        if j<0 or j>(N-1):
            continue #break 하면 안됨 
        
        if nums[i]==nums[j]:
            print(nums[i],nums[j])
            max_num= max(max_num,nums[i])

print(max_num)

#인덱스 차이가 K 이하면 폭발 
#폭발할애들 저장 
#폭발할 애들중에서 부여된 값이 가장 큰 것 찾기 

#폭발할 폭탄중 부여된 번호가 가장 큰 번호 출력