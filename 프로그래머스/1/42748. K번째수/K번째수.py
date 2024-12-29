def solution(array, commands):
    array = [0]+array # 인덱스 사용편의를 위함 
    answer =[] 
    
    for i,j,k in commands:
        new = array[i:j+1]
        new.sort()
        new= [0]+new
        answer.append(new[k])
    
    return answer












# answer = []
    
#     for comm in commands :
#         i=comm[0]
#         j=comm[1]
#         k=comm[2]
        
#         new_arr = array[i-1:j]
#         new_arr.sort()
#         answer.append(new_arr[k-1])
    