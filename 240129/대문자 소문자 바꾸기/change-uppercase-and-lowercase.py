A =input()

for i in A:
    if 'a'<= i <= 'z':
        print(i.upper(),end="")
    else:
        print(i.lower(),end="")