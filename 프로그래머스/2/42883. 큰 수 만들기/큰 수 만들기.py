def solution(number, k):
    # 앞의것이 뒤에꺼보다 커야한다
    # 뒤에가 더크면 지우기 개수 맞출때까지 
    cnt = 0 
    num_list = list(map(int,list(number)))
    stack = [] 
    i=0
    while cnt < k : #삭제할거 다 삭제
        if i >= len(num_list):
            # 다 못삭제했는데 값이 길어지면 뒤에꺼 다삭제 하는걸로가야함... 
            for _ in range(k-cnt):
                stack.pop()
            break
        if stack ==[] or stack[-1] >= num_list[i]:
            stack.append(num_list[i])
            i+=1
        else:
            stack.pop()
            cnt +=1
    #추가할거 나머지 다추가 
    while i < len(num_list):
        stack.append(num_list[i])
        i +=1
    
    stack = list(map(str,stack))
    answer = "".join(stack)
    return answer