arr= input()
mo = input()

def f():
    num =-1 
    
    for n in range(len(arr)-len(mo)+1):
        flag = True
        for m in range(len(mo)):
            if arr[n+m] != mo[m]:
                flag = False
                break
        if flag:
            num = n 
            break
    return num

print(f())