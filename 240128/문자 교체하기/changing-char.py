a,b = input().split()

a,b= list(a),list(b)

b[0],b[1] = a[0],a[1]

b = "".join(b)

print(b)