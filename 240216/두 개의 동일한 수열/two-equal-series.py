n= int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

A.sort()
B.sort()

if A==B:
    print("Yes")
else:
    print("No")


"""
zip(리스트1,리스트2) 해서 순서대로 묶은다음에
다시 언패킹해서 
각 원소를 비교할수도있군.. 

def equal():
    # n개의 원소를 순서대로 봤을 때
    # 전부 동일한 경우에만 일치합니다.
    # 단 하나라도 다르다면, false입니다.
    for elem1, elem2 in zip(a, b):
        if elem1 != elem2:
            return False
    
    return True
"""