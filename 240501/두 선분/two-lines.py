x1,x2,x3,x4 = map(int,input().split())

isCrossed= False 
if x3 <= x1 <= x4:
    isCrossed= True
elif x3 <= x2 <= x4:
    isCrossed= True
elif x1 <= x3 <= x2:
    isCrossed= True
elif x1 <= x4 <= x2:
    isCrossed= True

if isCrossed:
    print("intersecting")
else:
    print("nonintersecting")