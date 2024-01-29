arr = input()

for i in arr:
    if i.isalpha():
        print(i.lower(),end="")
    elif i.isdigit():
        print(i,end="")