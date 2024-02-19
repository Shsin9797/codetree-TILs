class Info:
    def __init__(self,code,color,sec):
        self.code = code
        self.color = color 
        self.sec = sec 

code,color,sec= input().split()
sec =int(sec)

info = Info(code,color,sec)
print(f"code : {info.code}")
print(f"color : {info.color}")
print(f"second : {info.sec}")