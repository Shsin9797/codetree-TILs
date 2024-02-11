arr= input()
mo = input()

def f():
    num =-1 
    for n in range(len(arr)-len(mo)+1):
        for m in range(len(mo)):
            if arr[n+m] != mo[m]:
                break
            num = n 
    return num

print(f())