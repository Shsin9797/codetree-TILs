class Info():
    def __init__(self,code,area,time):
        self.code = code
        self.area = area
        self.time = time 

c,a,t = input().split()
t=int(t)

info = Info(c,a,t)
print("secret code :",info.code)
print("meeting point :",info.area)
print("time :", info.time)