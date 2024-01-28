s,q = input().split()
q =int(q)
s = list(s)
for _ in range(q):
    n,a,b = input().split()
    n= int(n)

    if n == 1:
        a,b=int(a)-1,int(b)-1
        
        s[a],s[b] = s[b],s[a]
    elif n == 2:
        for i in range(len(s)):
            charA= a
            charB= b
            if s[i] == charA:
                s[i] = charB
    print("".join(s))